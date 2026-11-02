// Psychology PhD Explorer: everything that differs from the linguistics site.
// Copied over src/lib/discipline.ts by pipeline/export_site.py.
export const DISCIPLINE = 'psych';
export const SITE = {
  name: 'Psychology PhD Explorer',
  nameZh: '心理学博士项目探索',
  owner: { name: 'Junyi Chen', url: 'https://github.com/Junyi-Ch', email: 'apc003@ucsd.edu' },
  repo: 'Junyi-Ch/psych_phd_finder',
  sibling: { name: 'Linguistics PhD Explorer', url: 'https://junyi-ch.github.io/linguistics_phd_finder/' },
  description: 'Find psychology, cognitive science and neuroscience faculty at the top 100 U.S. universities whose research matches yours. Matching runs in your browser.',
  networkDescription: 'Browse psychology faculty as a map: people whose research is similar sit close together.',
  csvName: 'psychology-phd-shortlist.csv',
};
// '' = the theme draws its own mark (a ring with a marigold dot)
export const LOGO = '';
export const FIELDS = ['PSY', 'COGSCI', 'NEURO'] as const;
export type Field = (typeof FIELDS)[number];
export const FIELD_LABELS: Record<Field, { en: string; zh: string }> = {
  PSY: { en: 'Psychology departments', zh: '心理学系' },
  COGSCI: { en: 'Cognitive science', zh: '认知科学' },
  NEURO: { en: 'Neuroscience programs', zh: '神经科学项目' },
};
export const FIELD_SHORT: Record<string, string> = { PSY: 'Psychology', COGSCI: 'Cognitive science', NEURO: 'Neuroscience' };
export const RANKINGS = {
  qs: { name: '', short: '', url: '', tops: [] as number[] },
  us: { name: 'U.S. News Best National Universities 2027', short: 'U.S. News 2027 (whole university)', url: 'https://www.usnews.com/best-colleges/rankings/national-universities', tops: [25, 50, 100] },
} as const;
export const HAS_QS = false;
export const GLYPH: Record<string, string> = {};
// Research areas folded into eight families, used to colour the Network map (fixed order = fixed colour).
export const GROUPS = [
  { k: 'cognition', en: 'Perception & cognition', zh: '知觉与认知', topics: ['T_PERCEPTION', 'T_ATTENTION', 'T_MEMORY', 'T_ACTION'] },
  { k: 'thought', en: 'Language & thought', zh: '语言与思维', topics: ['T_LANGUAGE', 'T_DECISION', 'T_CONCEPTS'] },
  { k: 'affect', en: 'Emotion & motivation', zh: '情绪与动机', topics: ['T_EMOTION', 'T_MOTIVATION'] },
  { k: 'social', en: 'Social & personality', zh: '社会与人格', topics: ['T_SOCIAL_COG', 'T_RELATIONSHIPS', 'T_GROUPS_CULTURE', 'T_PERSONALITY'] },
  { k: 'development', en: 'Development & lifespan', zh: '发展与毕生', topics: ['T_DEVELOPMENT', 'T_AGING', 'T_EDUCATION'] },
  { k: 'health', en: 'Health & mental health', zh: '健康与心理健康', topics: ['T_HEALTH', 'T_MENTAL_HEALTH'] },
  { k: 'brain', en: 'Brain & behavior', zh: '脑与行为', topics: ['T_COG_NEURO', 'T_SYSTEMS_NEURO', 'T_EVOLUTION'] },
  { k: 'methods', en: 'Computation, methods & applied', zh: '计算、方法与应用', topics: ['T_COMPUTATIONAL', 'T_QUANT', 'T_APPLIED'] },
] as const;
export const EXAMPLES: string[] = [
  'I want to study how children learn the meanings of new words from conversation and social cues, using looking-time and eye-tracking experiments with toddlers.',
  'My interest is in how stress during adolescence changes reward learning and risk taking, using fMRI and computational models of reinforcement learning.',
  'I study how people spread and correct misinformation online, combining large-scale social media data with survey experiments on political polarization.',
  'I want to research how bilinguals control which language they speak, using reaction-time tasks, EEG and studies of code-switching.',
  'How does working memory capacity limit visual attention? I use psychophysics and computational models with adult participants.',
];
export const EXAMPLE_LABELS: string[] = ['Word learning in toddlers', 'Adolescent stress & reward', 'Misinformation online', 'Bilingual language control', 'Working memory & attention'];
export const I18N: Record<string, { en: string; zh: string }> = {
  brand: { en: 'Psychology PhD Explorer', zh: '心理学博士项目探索' },
  hero_eyebrow: { en: 'Psychology · Cognitive science · Neuroscience', zh: '心理学 · 认知科学 · 神经科学' },
  match_h1: { en: 'Find the labs that fit your research', zh: '找到契合你研究方向的实验室' },
  match_h1a: { en: 'Find the labs that fit', zh: '找到契合' },
  match_h1b: { en: 'your research', zh: '你研究方向' },
  match_h1c: { en: '', zh: '的实验室' },
  match_lede2: { en: 'Describe what you want to study. We compare it with every psychology, cognitive science and neuroscience faculty profile at the top 100 U.S. universities.', zh: '描述你想研究的问题和方法，我们会把它与美国前 100 所大学心理学、认知科学和神经科学教师的研究逐一比较。' },
  match_label: { en: 'What do you want to study?', zh: '你想研究什么？' },
  match_placeholder: { en: 'e.g. How adolescents learn from reward and punishment, and how stress changes it. I would like to use fMRI and daily-life sampling.', zh: '例如：青少年如何从奖励和惩罚中学习，以及压力如何改变这一过程。我希望用 fMRI 和日常生活经验取样。' },
  fshort_PSY: { en: 'Psychology', zh: '心理学系' },
  fshort_COGSCI: { en: 'Cognitive science', zh: '认知科学' },
  fshort_NEURO: { en: 'Neuroscience', zh: '神经科学' },
  field_PSY: { en: 'Psychology departments', zh: '心理学系' },
  field_COGSCI: { en: 'Cognitive science', zh: '认知科学' },
  field_NEURO: { en: 'Neuroscience programs', zh: '神经科学项目' },
  net_lede2: { en: 'See how faculty at the top 100 U.S. universities relate to each other: people whose research is similar sit close together. Click anyone on the map.', zh: '看看美国前 100 所大学的教师之间如何关联：研究方向相近的人会靠在一起。点击地图上的任何人查看详情。' },
  net_color2: { en: 'Dot colour = main research area (click to hide or show):', zh: '点的颜色 = 主要研究领域（点击可隐藏或显示）：' },
  net_color: { en: 'Colour = main research area', zh: '颜色 = 主要研究领域' },
  net_other: { en: 'No research-area label', zh: '无研究领域标签' },
};
