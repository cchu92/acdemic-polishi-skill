# Academic De-AI Rewrite

`Academic De-AI Rewrite` 是一个面向英文 `academic paper` 场景的改写 skill。

它的目标不是把论文改得更“华丽”或更像通用润色器，而是把带有明显 AI 痕迹的学术英文，改写成更自然、更克制、更符合真实研究者写作习惯的表达，同时严格保留技术含义、术语体系、公式、引用和 LaTeX 结构。

## 1. 这是什么

这个 skill 主要解决以下问题：

- 语法正确，但段落推进发平
- 连接词机械，句式模板化
- 抽象名词堆叠，信息密度不高
- 同义重复，过度解释
- 读起来像 AI 在“解释给机器听”，而不是同行交流

它适用于：

- 英文论文段落改写
- LaTeX 论文文本自然化改写
- introduction / methods / results / discussion 等常见论文章节
- 局部句子、局部段落、整段文字的去 AI 化重写
- 需要保留修改记录的写作工作流

它不适用于：

- grant proposal
- cover letter
- marketing copy
- 从零生成论文内容
- 修改数学结论或编造技术论证

## 2. 项目结构

```text
.
├── README.md
├── Spec.md
└── academic-de-ai-rewrite/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── rewrite-patterns.md
    │   ├── section-guidance.md
    │   ├── latex-safety.md
    │   └── logging.md
    └── scripts/
        └── append_modification_log.py
```

核心文件说明：

- `academic-de-ai-rewrite/SKILL.md`
  skill 的主工作流、边界和输出规则
- `academic-de-ai-rewrite/references/rewrite-patterns.md`
  常见 AI 痕迹及对应改写策略
- `academic-de-ai-rewrite/references/section-guidance.md`
  按论文章节区分改写节奏
- `academic-de-ai-rewrite/references/latex-safety.md`
  LaTeX 与公式保护规则
- `academic-de-ai-rewrite/references/logging.md`
  持久化日志规则
- `academic-de-ai-rewrite/scripts/append_modification_log.py`
  将修改记录追加到 Markdown 日志文件

## 3. 输出形式

默认输出分为两部分：

### Part 1 [LaTeX]

输出改写后的英文文本，保持 LaTeX、公式、符号、引用结构不变。

### Part 2 [Modification Log]

简要说明本次主要改了什么，例如：

- 删除机械连接词
- 压缩冗余表达
- 改善段落推进
- 仅局部修改，不扩大重写范围

## 4. 持久化日志

这个 skill 支持把每次改写记录持久化到文件中。

默认日志路径：

```text
./rewrite-logs/academic-de-ai-rewrite-log.md
```

如果你指定了其他路径，则以你给定的路径为准。

每条日志默认记录：

- 时间戳
- 修改范围
- 源文件路径
- 输出文件路径
- 修改模式：`full` / `partial` / `no-op`
- 修改摘要
- 原文片段
- 改写后片段
- 备注

手动追加日志的脚本：

```bash
python3 academic-de-ai-rewrite/scripts/append_modification_log.py \
  --scope "Introduction paragraph 2" \
  --edit-mode partial \
  --source-path ./paper/main.tex \
  --summary "Removed mechanical lead-in" \
  --summary "Compressed redundant wording" \
  --original-file /tmp/original.txt \
  --revised-file /tmp/revised.txt
```

## 5. 如何使用

### 5.1 在 Codex 中使用

Codex 原生适合这个 skill，因为它可以显式调用 skill 并按 `SKILL.md` 规则执行。

如果你希望全局可发现，先把 skill 目录放到：

```bash
${CODEX_HOME:-$HOME/.codex}/skills/
```

例如：

```bash
cp -R academic-de-ai-rewrite "${CODEX_HOME:-$HOME/.codex}/skills/"
```

然后在 Codex 中直接调用：

```text
Use $academic-de-ai-rewrite to rewrite the following introduction paragraph into more natural academic English. Preserve technical meaning and LaTeX structure. Return Part 1 [LaTeX] and Part 2 [Modification Log].
```

如果你只想改局部：

```text
Use $academic-de-ai-rewrite to revise only the marked sentence below. Keep all surrounding text unchanged. Return Part 1 [LaTeX] and Part 2 [Modification Log].
```

如果你希望自动保留持久化日志：

```text
Use $academic-de-ai-rewrite to rewrite the paragraph below and keep a persistent log at ./rewrite-logs/academic-de-ai-rewrite-log.md.
```

### 5.2 在 Claude Code 中使用

`Claude Code` 不一定原生识别 Codex skill 格式，但可以把这个 skill 当成一组明确的操作规范来使用。

最稳妥的方式是：

1. 让 agent 读取 `academic-de-ai-rewrite/SKILL.md`
2. 需要时再读取 `references/` 下的相关文件
3. 按该规则执行改写
4. 如需持久化日志，再执行 `scripts/append_modification_log.py`

可直接使用的提示词：

```text
Read ./academic-de-ai-rewrite/SKILL.md and use it as the rewrite policy for the text below.
If needed, also read:
- ./academic-de-ai-rewrite/references/rewrite-patterns.md
- ./academic-de-ai-rewrite/references/section-guidance.md
- ./academic-de-ai-rewrite/references/latex-safety.md
- ./academic-de-ai-rewrite/references/logging.md

Rewrite only the provided paragraph into more natural academic English.
Preserve technical meaning, terminology, citations, formulas, and LaTeX structure.
Return:
1. Part 1 [LaTeX]
2. Part 2 [Modification Log]
Also append a persistent log entry to ./rewrite-logs/academic-de-ai-rewrite-log.md.
```

如果你只想局部修改，把提示改成：

```text
Rewrite only the marked sentence. Do not edit surrounding text unless strictly necessary for coherence.
```

### 5.3 在 Cursor 中使用

在 `Cursor` 里，推荐把这个 skill 当成项目级写作规则或 agent 工作说明来使用。

常见做法有两种：

1. 在 Agent/Composer 对话中直接让它读取 `SKILL.md`
2. 把 `SKILL.md` 的核心规则提炼成项目规则，再配合本仓库文件使用

直接在 Cursor Agent 中可用的提示词：

```text
Use ./academic-de-ai-rewrite/SKILL.md as the rewrite spec for this task.
Only rewrite the paragraph I provide.
Preserve all technical meaning, formulas, citations, and LaTeX syntax.
Return:
1. Part 1 [LaTeX]
2. Part 2 [Modification Log]

If I ask for persistent logging, use:
./academic-de-ai-rewrite/scripts/append_modification_log.py
to append the change record to:
./rewrite-logs/academic-de-ai-rewrite-log.md
```

如果你在 Cursor 里处理整篇论文的局部片段，建议明确告诉 agent：

- 改整段还是只改一句
- 是否允许重排句序
- 是否需要日志落盘
- 日志路径是什么

## 6. 推荐使用模式

### 模式 A：只要改写结果

适合一次性润色。

```text
Use this skill to rewrite the paragraph for a more natural academic tone. No persistent file log is needed.
```

### 模式 B：改写 + 响应内日志

适合人工快速审阅。

```text
Rewrite the paragraph and return Part 1 [LaTeX] plus Part 2 [Modification Log].
```

### 模式 C：改写 + 持久化日志

适合长期论文迭代和版本审阅。

```text
Rewrite the paragraph, return Part 1 [LaTeX] and Part 2 [Modification Log], and append a persistent log entry to ./rewrite-logs/academic-de-ai-rewrite-log.md.
```

## 7. 局部修改建议

如果你不想 agent 擅自扩大重写范围，建议在提示词里写清楚：

- `only rewrite the marked sentence`
- `edit only this paragraph`
- `keep all surrounding text unchanged`
- `local edit only`
- `minimal intervention`

这样可以让 skill 保持局部改写，同时把范围限制写入 `Modification Log` 和持久化日志。

## 8. 一句话总结

这个项目的核心不是“把英文改得更高级”，而是“把 AI 味明显但技术上正确的 academic prose，改成更像真实研究者写出来的文本”，并且支持可审阅、可追踪、可持久化的修改记录。
