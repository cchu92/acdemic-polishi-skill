Project Specification
Project Name

Academic Polish / Academic De-AI Rewrite

1. Project Overview

本项目旨在设计并实现一个面向**学术论文（academic paper）**场景的文本改写 Skill，用于将 AI 生成或 AI 痕迹明显的英文论文文本，重写为更自然、更克制、更符合真实学术写作习惯的英文表达。

该项目不追求“更华丽”或“更像润色器”，而强调以下目标：

保持技术含义不变；
优先优化段落和论证结构；
去除 AI 文本常见的机械感与模板感；
输出更符合专业研究者阅读习惯的学术英语；
适用于已有一定写作经验、但希望提升自然度与可读性的研究者。

本项目仅适用于 academic paper，不覆盖 grant proposal、cover letter、marketing copy 或 general English polishing。

2. Problem Statement

当前 AI 生成的学术英文文本普遍存在以下问题：

结构正确但论证发平
句子本身语法正确，但整段缺乏自然推进，像把若干“正确句子”并排放在一起。
模板化表达明显
过度依赖固定连接词、固定句式、固定总结方式，导致文本呈现出强烈的模型痕迹。
过度解释
将本领域读者已默认理解的逻辑讲得过满，读起来像“在解释给机器听”，而不是同行交流。
抽象名词堆叠
使用大量空泛名词来制造“正式感”，但信息密度偏低，表达落点不清。
冗余与伪高级感
同一含义被重复换说法，或者使用看似高级但不自然的学术表达，降低可读性。
段落节奏单一
句长、句势、段落开头与结尾都过于均质，造成“AI 味”。

现有通用润色工具大多聚焦于语法纠错、词汇升级或表面正式化，无法针对上述问题做出结构层面、学术场景化、克制而精准的处理。

3. Project Goal

本项目的目标是构建一个 Skill，使其能够：

识别 academic paper 文本中的典型 AI 痕迹；
在不改变技术内容的前提下，进行结构性和风格性的克制改写；
将“语法正确但机械化”的文本，重写为“自然、专业、可投稿”的学术英语；
对已有一定写作能力的用户提供实用、轻量、针对性强的改写支持，而不是基础英语教学。
4. Target Users
Primary Users
非英语母语的研究者
已有一定 academic paper 写作经验
已能写出基本正确的英文论文内容
希望减少 AI 痕迹并提升自然度、可读性和专业感
Non-Target Users

本项目不以以下用户为主要对象：

完全没有学术写作经验的初学者
需要从零学习 academic writing 的用户
主要写作场景为 grant proposal、商业文案或科普文本的用户
需要内容生成而非内容改写的用户
5. Scope
In Scope

本项目支持以下任务：

对英文 academic paper 段落进行去 AI 化改写
对 LaTeX 论文文本进行自然化学术表达改写
保留数学公式、技术符号和引用结构
优化段落内部结构与句间衔接
减少模板化学术表达与机械连接词
压缩抽象、冗余和过度解释
Out of Scope

本项目不负责：

生成整篇论文内容
编造技术论证或实验结果
修改数学公式与技术结论
做深度学术内容审稿
替用户决定研究贡献是否成立
撰写 grant proposal、cover letter、review response
做纯语法纠错型语言学习辅导
6. Core Design Principles
6.1 Structure First

改写优先级应放在结构与论证推进，而非词汇替换。

6.2 De-AI at the Discourse Level

去 AI 味不应停留在禁词替换层面，而应处理：

句法模板化
结构发平
过度解释
抽象表达堆叠
冗余重复
段落节奏机械
6.3 Minimal but Effective Editing

坚持“必要、克制、有效”的修改原则。
如果原文已经自然，则不应为了显示改动而过度重写。

6.4 Preserve Authorial Meaning

不得改变技术含义、结论方向、逻辑立场或术语体系。

6.5 Field-Appropriate Academic Tone

输出应符合 academic paper 场景中的真实学术表达，而不是一般“正式英语”或“润色器腔”。

7. Key Pain Points to Address

Skill 在执行时，重点针对以下高频问题：

机械连接词
例如：First and foremost, It is worth noting that
句式重复
例如：连续使用 This study..., This work..., The results indicate...
抽象度过高
例如：连续使用 framework, methodology, effectiveness, capability
同义重复
同一个意思换不同措辞重复表达
过度解释
把隐含逻辑全部显性写出，破坏自然阅读感
空泛评价
听起来“很强”但没有实质信息支撑的评价性语言
段落节奏发平
句长、语气、推进方式都过于均匀
局部自然、整体不自然
每句单看没问题，但整段不像真实研究者写作
8. Functional Requirements
FR1. Input Understanding

系统必须先通读整段或全文，识别：

段落功能
核心论点
句间关系
是否存在整体结构发平的问题
FR2. Structural Rewriting

在必要时，系统应能调整句序与信息组织，使段落推进更自然，但不得改变技术含义。

FR3. De-AI Rewriting

系统应能针对 AI 风格缺陷进行改写，包括但不限于：

删除机械连接词
压缩抽象表达
删除同义重复
减少过度解释
调整句子节奏
FR4. Minimal Intervention

若原文已自然，则系统应保留原文或仅进行极少量改动。

FR5. LaTeX Preservation

系统必须：

保留 $...$ 数学公式
保留变量、标签、引用
不引入无关 LaTeX 指令
正确转义 %, _, &
FR6. Modification Logging

系统输出中应说明主要修改动作，帮助用户理解改写重点。

9. Non-Functional Requirements
NFR1. Accuracy

不得篡改技术内容或引入新结论。

NFR2. Readability

改写后文本应更易于被母语专业读者接受。

NFR3. Naturalness

输出应避免明显 AI 痕迹，读起来更接近真实论文表达。

NFR4. Restraint

不应把文本改得过度 polished 或过度华丽。

NFR5. Consistency

同一段文本中的术语和语气应保持一致。

10. Input Specification

用户输入通常为以下之一：

一段英文 academic paper 文本
一段 LaTeX 格式论文内容
多段需连续改写的论文章节内容

用户常见意图包括：

润色
重写
去 AI 化
提升自然度
更像母语研究者写作
更适合投稿表达
11. Output Specification

输出应严格分为两部分：

Part 1 [LaTeX]
输出改写后的全英文文本
保持 LaTeX 与公式结构不变
不插入解释性批注
Part 2 [Modification Log]
简要说明主要修改动作
若无需修改，明确说明原文已自然，建议保留
12. Success Criteria

如果该 Skill 有效，则输出应满足以下标准：

技术含义未改变
段落推进更自然
明显 AI 痕迹减少
抽象与冗余表达被压缩
段落节奏更接近真实研究者写作
输出没有变成“另一个更高级的 AI 腔”
用户感觉修改是必要的，而不是表演性的
13. Failure Cases

以下情况可视为 Skill 失败：

改写后技术意思发生偏移
为了“自然”而删掉必要信息
输出变得过于华丽或不符合学术语域
大量替换词汇，但段落层面问题未被解决
过度重写，抹掉原文本来已有的优点
修改日志笼统，无法反映真实改动重点
14. Representative Use Cases
Use Case 1

用户提供 introduction 中一段 AI 生成的英文背景介绍，语法正确，但读起来模板感强。
Skill 应保留学术内容，压缩空泛表达，减少机械过渡，使其更像真实论文引言。

Use Case 2

用户提供 method section 中一段 LaTeX 内容，存在抽象名词堆叠与同义重复。
Skill 应在不改动公式与术语的前提下，使表达更具体、更紧凑。

Use Case 3

用户提供 result discussion 中一段文字，句句正确但整段节奏发平。
Skill 应通过局部重组与句法变化改善段落推进，而不是简单替换几个词。

15. Product Positioning

本项目不是：

通用英语润色器
语法纠错器
学术内容生成器
论文写作教程

本项目是一个：
面向 academic paper 的、聚焦 AI 痕迹消除与自然学术表达重写的轻量型专业 Skill

其核心价值在于：
不把文本改得更“像润色器”，而是改得更像真实研究者。

16. Future Extensions

在当前版本之外，未来可考虑扩展：

按论文章节类型进行更细粒度改写策略
增加领域特定用语偏好
区分 introduction / methods / discussion 的不同节奏要求
增加“只诊断不改写”的模式