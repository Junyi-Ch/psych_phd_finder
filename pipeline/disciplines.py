"""Per-discipline settings shared by the pipeline scripts (scrape_local, label_local, build).

Pick one with --discipline <id> or the DISCIPLINE environment variable (default: linguistics).
Linguistics keeps its original file layout (data/, pipeline/taxonomy.json); other disciplines live in data/<id>/.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LING_SUMMARY = """You describe a university researcher's work for a website that helps PhD applicants in linguistics find advisors.
Use ONLY the profile text given. Do not use outside knowledge about the person. If the profile says little, say little.

Return JSON with:
- summary: ONE sentence, at most 200 characters, present tense, without the person's name, saying what they study and how.
  Example: "Studies tone and intonation in Bantu languages through fieldwork and acoustic analysis."
- summary_zh: the same sentence in natural Chinese (use standard linguistics terms, e.g. 音系学, 句法学, 语义学, 社会语言学).
- keywords: 5 to 10 specific lowercase terms from the profile (phenomena, languages, methods), e.g. "tone sandhi", "visual world paradigm", "quechua".
- confidence: "high" if the profile describes their research in detail, "medium" if briefly, "low" if almost not at all.
"""

LING_LABEL_INTRO = """You tag a linguistics researcher's profile with codes from a fixed list, for a search website.
Use ONLY what the profile, summary and keywords say. Choose the codes that clearly apply; most people get 1-3 per list.

- topic: 1 to 4 subfields they work in. primary_topic: the single main one.
- approach: methods they use. data: kinds of data they work with. setting: populations or settings they study (often none).
- region: languages they study. Only languages actually named or clearly implied (e.g. "Quechua" -> R_AMERICAS_INDIGENOUS,
  "Spanish" -> R_ROMANCE, "ASL" -> R_SIGN). R_ENGLISH only when English itself is studied. Leave empty if no language is named.

Example: profile about "variation in Boston Spanish, sociophonetics, interviews with speakers"
-> topic [T_SOCIOLING, T_PHONETICS], primary_topic T_SOCIOLING, approach [A_VARIATIONIST], data [D_SPOKEN_CORPORA, D_SPEECH_AUDIO],
   setting [S_SPEECH_COMMUNITIES, S_BILINGUAL_HERITAGE], region [R_ROMANCE]
"""

PSY_SUMMARY = """You describe a university researcher's work for a website that helps PhD applicants in psychology, cognitive science
and neuroscience find advisors. Use ONLY the profile text given. Do not use outside knowledge about the person.
If the profile says little, say little.

Return JSON with:
- summary: ONE sentence, at most 200 characters, present tense, without the person's name, saying what they study and how.
  Example: "Studies how children learn words from social cues, using eye-tracking and looking-time experiments with infants."
- summary_zh: the same sentence in natural Chinese (use standard psychology terms, e.g. 认知神经科学, 发展心理学, 社会认知, 工作记忆).
- keywords: 5 to 10 specific lowercase terms from the profile (phenomena, methods, populations, species), e.g. "working memory", "fmri", "zebra finch".
- confidence: "high" if the profile describes their research in detail, "medium" if briefly, "low" if almost not at all.
- psych_relevant: true if the research is about mind, brain or behavior in a way a psychology, cognitive science or neuroscience
  PhD applicant would study (perception, cognition, emotion, social behavior, development, brain systems for behavior, animal behavior).
  false when the main focus is molecules, cells, genes, disease mechanisms or medical treatment, even if behavior is mentioned
  in passing, and for work outside these fields.
- clinical_role: true if the person's research and training role is clinical psychology (therapy, assessment, treatment trials,
  clinical supervision, a clinical psychology program). false otherwise, including people who study mental health mechanisms
  without a clinical training role.
"""

PSY_LABEL_INTRO = """You tag a psychology, cognitive science or neuroscience researcher's profile with codes from a fixed list, for a search website.
Use ONLY what the profile, summary and keywords say. Pick a code only when the profile clearly says so; it is better to leave a
list short or empty than to guess. Most people get 1-3 topic codes and 1-3 method codes.

- topic: 1 to 4 research areas. primary_topic: the single main one.
- approach: methods they actually name. data: real-world domains the work connects to (often none). setting: the people they study
  (leave empty for animal-only research). region: species and systems studied (R_HUMANS for human participants;
  animals only when named, e.g. "mice" -> R_RODENTS, "macaques" -> R_PRIMATES).

Strict rules for codes that are easy to over-use:
- T_DEVELOPMENT only when infants, children or adolescents are studied. Adults, college students or "development of a scale" do not count.
- T_COG_NEURO only when the work measures the human brain (fMRI, EEG, MEG, brain stimulation, patients with brain lesions).
- T_SYSTEMS_NEURO only for neural circuits or brain recordings in animals.
- A_COMP_MODEL only when the profile names computational, mathematical, Bayesian, reinforcement-learning or neural-network models.
  Statistics such as regression or structural equation modeling are not A_COMP_MODEL (use A_STATS only for developing new methods).
- A_BEHAVIORAL only for laboratory experiments; surveys are A_SURVEY, therapy or prevention trials are A_FIELD.
- R_MACHINES only when artificial agents or neural-network models are themselves studied.
"""

LING_EVIDENCE = None  # label_local keeps its own language regexes for linguistics

PSY_EVIDENCE = {
    "R_HUMANS": r".",
    "R_PRIMATES": r"primate|monkey|macaque|marmoset|rhesus|chimpanzee|bonobo|apes?\b|baboon|lemur",
    "R_RODENTS": r"\bmice\b|\bmouse\b|\brats?\b|rodent|vole|hamster|gerbil",
    "R_BIRDS": r"\bbirds?\b|songbird|zebra finch|avian|pigeon|corvid|crows?\b|chick|starling|owl",
    "R_FISH_INVERT": r"zebrafish|\bfish\b|drosophila|fruit fl|\bflies\b|c\. ?elegans|worms?\b|\bbees?\b|honeybee|\bants?\b|octopus|cephalopod|insect|larva",
    "R_OTHER_ANIMALS": r"\bdogs?\b|canine|\bbats?\b|ferret|\bcats?\b|sheep|\bpigs?\b|horse|dolphin|whale|elephant|\bgoats?\b|lizard|frog|tadpole",
    "R_MACHINES": r"neural network|deep learning|robot|artificial agent|language model|\bllms?\b|\bai\b|artificial intelligence|machine learning",
}

# A code the small local model over-uses is kept only when the person's own text (profile, research areas, paper titles,
# keywords, summary) contains evidence for it.
PSY_CODE_EVIDENCE = {
    "T_DEVELOPMENT": r"infan|toddler|child|kid|preschool|adolesc|youth|teen|developmental|pediatric|school-age",
    "T_AGING": r"aging|ageing|older adult|elderly|late life|lifespan|dementia|alzheimer",
    "T_COG_NEURO": r"fmri|\bmri\b|eeg|\berps?\b|\bmeg\b|neuroimaging|brain imaging|human brain|cognitive neuroscien|affective neuroscien|social neuroscien|\btms\b|tdcs|brain stimulation|lesion|neuropsych|brain (activity|networks?|function|regions?|responses?|mechanisms)|electrophysiolog|intracranial|ecog",
    "T_SYSTEMS_NEURO": r"circuit|rodent|\bmice\b|\bmouse\b|\brats?\b|monkey|macaque|primate|neurons?|electrophysiolog|optogenet|songbird|zebrafish|drosophila|calcium imaging|spik",
    "T_COMPUTATIONAL": r"computational|model|bayesian|reinforcement learning|neural network|machine learning|artificial intelligence|\bai\b|simulation|algorithm",
    "T_QUANT": r"quantitative|psychometric|statistic|measurement|meta-analy|replica|methodolog|latent|structural equation|multilevel|bayesian",
    "T_LANGUAGE": r"language|linguist|speech|reading|word|sentence|bilingual|literacy|vocabular|communicat|conversation|sign language",
    "T_PERCEPTION": r"percept|vision|visual|auditory|hearing|touch|haptic|olfact|smell|taste|multisensory|psychophysic|color|motion|face",
    "T_ACTION": r"motor|movement|action|grasp|reach|gesture|embodi|locomot|posture|sensorimotor",
    "T_EVOLUTION": r"evolution|comparative|primate|animal cognition|species",
    "T_EDUCATION": r"education|school|classroom|student|teach|reading instruction|math|stem|learning sciences|literacy",
    "T_APPLIED": r"organiz|workplace|employee|personnel|leadership|human factors|ergonomic|engineering psych|industrial|team|aviation|driving|interface",
    "A_COMP_MODEL": r"computational|model(s|ing|ling)? of|bayesian|reinforcement learning|neural network|drift.diffusion|simulation|formal model|cognitive model|agent-based|deep learning",
    "A_ML": r"machine learning|deep learning|neural network|large language model|\bllms?\b|artificial intelligence|\bai\b|natural language processing",
    "A_BEHAVIORAL": r"experiment|laborator|\blab\b|task|reaction time|paradigm|stimul|trial",
    "A_PSYCHOPHYSICS": r"psychophysic|threshold|perceptual (judg|discrim)|contrast sensitivity|detection",
    "A_EYE_TRACKING": r"eye|gaze|pupil|saccad|fixation",
    "A_FMRI": r"fmri|\bmri\b|neuroimaging|brain imaging|bold|diffusion tensor|connectivity",
    "A_EEG_MEG": r"\beeg\b|\berps?\b|\bmeg\b|electroenceph|event-related potential|magnetoenceph|oscillat",
    "A_NEUROPSYCH": r"neuropsych|lesion|patient|\btms\b|tdcs|stimulation|brain injury|stroke|aphasia|epilep",
    "A_ANIMAL_NEURO": r"electrophysiolog|recording|calcium imaging|single.unit|in vivo|two-photon|neuropixel|patch.clamp",
    "A_CIRCUIT_TOOLS": r"optogenet|chemogenet|dreadd|pharmacolog|viral|knockout|transgenic|drug",
    "A_PHYSIOLOGY": r"physiolog|heart rate|cortisol|hormon|skin conductance|autonomic|immune|inflammat|blood pressure|biomarker",
    "A_GENETICS": r"genetic|twin|heritab|genome|polygenic|\bdna\b|gene",
    "A_SURVEY": r"survey|questionnaire|self-report|scale|interview|panel|national sample|measure",
    "A_DAILY_LIFE": r"daily|ecological momentary|\bema\b|experience sampling|smartphone|wearable|ambulatory|diary|passive sensing|social media data|big data",
    "A_LONGITUDINAL": r"longitudinal|cohort|over time|prospective|follow-up|trajector|panel",
    "A_FIELD": r"intervention|randomi[sz]ed|trial|field experiment|prevention|program evaluation|implementation|treatment",
    "A_OBSERVATION": r"observ|interview|qualitative|ethnograph|naturalistic|video|coding",
    "A_STATS": r"statistic|method|meta-analy|replica|psychometric|measurement|open science|reproducib",
}

CONFIG = {
    "linguistics": {"data": ROOT / "data", "taxonomy": ROOT / "pipeline" / "taxonomy.json",
                    "probes": ROOT / "pipeline" / "probes.json", "glossary": ROOT / "pipeline" / "glossary_zh.json",
                    "default_field": "LING", "universities": None, "psych_filter": False,
                    "summary_system": LING_SUMMARY, "label_intro": LING_LABEL_INTRO, "evidence": LING_EVIDENCE,
                    "extra_summary_fields": {}},
    "psych": {"data": ROOT / "data" / "psych", "taxonomy": ROOT / "data" / "psych" / "taxonomy.json",
              "probes": ROOT / "data" / "psych" / "probes.json", "glossary": ROOT / "pipeline" / "glossary_zh.json",
              "default_field": "PSY", "universities": ROOT / "data" / "psych" / "universities.tsv", "psych_filter": True,
              "summary_system": PSY_SUMMARY, "label_intro": PSY_LABEL_INTRO, "evidence": PSY_EVIDENCE,
              "extra_summary_fields": {"psych_relevant": {"type": "boolean"}, "clinical_role": {"type": "boolean"}},
              "code_evidence": PSY_CODE_EVIDENCE},
}

def current():
    d = os.environ.get("DISCIPLINE", "linguistics")
    if d not in CONFIG:
        raise SystemExit(f"Unknown discipline {d!r}; choose one of {', '.join(CONFIG)}")
    return d, CONFIG[d]
