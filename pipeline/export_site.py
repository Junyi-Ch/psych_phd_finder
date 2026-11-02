"""Export a sibling site (e.g. psychology) from this shared codebase into its own repo folder.

    python pipeline/export_site.py --discipline psych --out ../psych_phd_finder
    python pipeline/build.py --discipline psych --out ../psych_phd_finder     # data, search index, logos

1. copies the shared site code (src/, public/, config, workflow, pipeline/) into OUT,
   leaving out this site's generated data (src/data, public/search, public/schools, og image);
2. copies disciplines/<d>/site/** over it (discipline.ts, theme, hero art, about page, favicon...);
3. copies the discipline's inputs from data/<d>/ (never raw scrapes);
4. points astro.config.mjs at the sibling repo's GitHub Pages path and renames the package.
Files in OUT that are not produced here (its .git, README, src/data written by build.py) are left alone.
"""
import argparse, fnmatch, json, os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITES = {
    'psych': {'repo': 'psych_phd_finder', 'package': 'psychology-phd-explorer', 'title': 'Psychology PhD Explorer'},
}
# shared code to copy (relative to ROOT)
CODE = ['src', 'public', 'astro.config.mjs', 'package.json', 'package-lock.json', 'tsconfig.json', '.github', '.gitignore', 'pipeline']
SKIP = [
    'src/data/*', 'public/search/*', 'public/schools/*', 'public/og.png',
    'pipeline/.cache*', '*/__pycache__*', '*.pyc', '.DS_Store', '*/.DS_Store',
]
DATA_KEEP = ['programs.json', 'fixes.json', 'taxonomy.json', 'universities.tsv', 'probes.json', 'glossary.json', 'relevance.json', 'labels/*', 'rosters/*']


def skipped(rel: str) -> bool:
    return any(fnmatch.fnmatch(rel, pat) for pat in SKIP)


def copy_file(src: Path, dst: Path) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and dst.read_bytes() == src.read_bytes():
        return False
    shutil.copyfile(src, dst)
    return True


def walk(base: Path):
    if base.is_file():
        yield base
        return
    for dp, dn, fn in os.walk(base):
        dn[:] = [d for d in dn if d not in ('node_modules', '__pycache__', '.cache')]
        for f in fn:
            yield Path(dp) / f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--discipline', required=True, choices=sorted(SITES))
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d, cfg = a.discipline, SITES[a.discipline]
    out = Path(a.out).expanduser().resolve()
    if out == ROOT or ROOT in out.parents:
        sys.exit('--out must be outside this folder')
    out.mkdir(parents=True, exist_ok=True)
    changed = 0
    # 1. shared code
    for item in CODE:
        for f in walk(ROOT / item):
            rel = f.relative_to(ROOT).as_posix()
            if skipped(rel):
                continue
            changed += copy_file(f, out / rel)
    # 2. discipline overrides
    over = ROOT / 'disciplines' / d / 'site'
    for f in walk(over):
        rel = f.relative_to(over).as_posix()
        changed += copy_file(f, out / rel)
    # 3. discipline inputs (no raw scrapes, no profile text)
    src_data = ROOT / 'data' / d
    for f in walk(src_data):
        rel = f.relative_to(src_data).as_posix()
        if any(fnmatch.fnmatch(rel, pat) for pat in DATA_KEEP):
            changed += copy_file(f, out / 'data' / d / rel)
    # 4. config: Pages path, package name, default discipline for npm run gen
    ac = out / 'astro.config.mjs'
    s = ac.read_text()
    s = re.sub(r"base: '/[^']*'", f"base: '/{cfg['repo']}'", s)
    s = re.sub(r'https://junyi-ch\.github\.io/[a-z_]+/', f"https://junyi-ch.github.io/{cfg['repo']}/", s)
    ac.write_text(s)
    rb = out / 'public' / 'robots.txt'
    if rb.exists():
        rb.write_text(re.sub(r'https://junyi-ch\.github\.io/[a-z_]+/', f"https://junyi-ch.github.io/{cfg['repo']}/", rb.read_text()))
    pj = out / 'package.json'
    p = json.loads(pj.read_text())
    p['name'] = cfg['package']
    p['scripts']['gen'] = f'python pipeline/build.py --discipline {d}'
    p['scripts'].pop('check:data', None)
    pj.write_text(json.dumps(p, indent=2, ensure_ascii=False) + '\n')
    pl = out / 'package-lock.json'
    l = json.loads(pl.read_text())
    l['name'] = cfg['package']
    if '' in l.get('packages', {}):
        l['packages']['']['name'] = cfg['package']
    pl.write_text(json.dumps(l, indent=2, ensure_ascii=False) + '\n')
    print(f'exported {d} to {out} ({changed} files changed)')
    print(f'next: python pipeline/build.py --discipline {d} --out {out}')


if __name__ == '__main__':
    main()
