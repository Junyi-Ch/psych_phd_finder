export const DIMS = ['topic', 'approach', 'data', 'setting', 'region'] as const;
export type Dim = (typeof DIMS)[number];
import { FIELDS, FIELD_LABELS, RANKINGS, GROUPS, HAS_QS, type Field } from './discipline';
export { FIELDS, FIELD_LABELS, RANKINGS, GROUPS, HAS_QS, type Field };
export const fieldLabel = (f: Field, lang: string) => (lang === 'zh' ? FIELD_LABELS[f]?.zh : FIELD_LABELS[f]?.en) || f;
export type LabelRef = { c: string; p: boolean };
export type Faculty = {
  id: string; name: string; u: string; dept: string; rank: string; title: string;
  profile: string | null; site: string | null; scholar: string | null;
  areas: string[]; summary: string; summary_zh: string; conf: string;
  labels: Record<Dim, LabelRef[]>; kw: string[]; src: string[]; scraped: string | null; v: number; fld: Field;
};
export type Unit = { name: string; field: Field; school: string | null; url: string | null; phd: string | null; phd_url: string | null; directory: string | null };
export type Program = {
  slug: string; name: string; short: string; city: string; state: string; lat: number; lng: number;
  domain: string | null; logo: string | null; guide: string[]; units: Unit[];
  n: number; ranks: Record<string, number>; notes: string;
  qs: string | null; us: string | null;
};
/** worst position a rank can mean: "17" -> 17, "=32" -> 32, "101-150" -> 150, "101+" -> 999, null -> null */
export function rankTop(r: string | null | undefined): number | null {
  if (!r) return null;
  if (r === '101+') return 999;
  const m = r.match(/(\d+)(?:-(\d+))?/);
  return m ? Number(m[2] || m[1]) : null;
}
export function rankText(r: string | null | undefined, lang = 'en'): string {
  if (!r) return lang === 'zh' ? '未上榜' : 'not ranked';
  if (r === '101+') return lang === 'zh' ? '100 名以外' : 'below 100';
  if (r.includes('-')) return r.replace('-', '–');
  return '#' + r.replace('=', '') + (r.startsWith('=') ? (lang === 'zh' ? '（并列）' : ' (tied)') : '');
}
export function passesRank(p: { qs: string | null; us: string | null }, qsMax: number, usMax: number) {
  if (qsMax) { const v = rankTop(p.qs); if (v == null || v > qsMax) return false; }
  if (usMax) { const v = rankTop(p.us); if (v == null || v > usMax) return false; }
  return true;
}
export type Taxonomy = { dimensions: Record<Dim, { label: string; label_zh: string; description: string; description_zh: string; labels: Record<string, string>; labels_zh: Record<string, string>; labels_short: Record<string, string>; labels_short_zh: Record<string, string> }> };

export const BASE = (import.meta.env.BASE_URL as string).replace(/\/+$/, '') + '/';
export const withBase = (p: string) => BASE + p.replace(/^\/+/, '');
export const initials = (name: string) => name.split(/\s+/).filter(Boolean).filter((w) => !/^\(.*\)$/.test(w)).slice(0, 2).map((w) => w[0]).join('').toUpperCase();
export const lastName = (name: string) => { const parts = name.replace(/,.*$/, '').trim().split(/\s+/); return parts[parts.length - 1] || name; };
export function labelText(tax: Taxonomy, dim: Dim, code: string, lang: string) {
  const d = tax.dimensions[dim];
  return (lang === 'zh' ? d.labels_short_zh?.[code] : d.labels_short?.[code]) || d.labels[code] || code;
}
export function labelFull(tax: Taxonomy, dim: Dim, code: string, lang: string) {
  const d = tax.dimensions[dim];
  return (lang === 'zh' ? d.labels_zh[code] : d.labels[code]) || code;
}
export function dimLabel(tax: Taxonomy, dim: Dim, lang: string) {
  const d = tax.dimensions[dim];
  return lang === 'zh' ? d.label_zh : d.label;
}
export const RANK_ORDER: Record<string, number> = { 'Professor': 0, 'Associate Professor': 1, 'Assistant Professor': 2, 'Faculty': 3 };
export const esc = (s: string) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!);

// an IPA-flavoured glyph for each person's main subfield, on a pastel tile (no photos are published)
function hash(s: string) { let h = 0; for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return Math.abs(h); }
// Person tiles were removed: they carried no information. Kept as a no-op so callers stay simple.
export function avatar(_f: Faculty, _lg = false) { return ''; }


