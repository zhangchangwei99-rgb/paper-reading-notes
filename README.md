# Paper Reading Notes · 学术文献研读与笔记

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/zhangchangwei99-rgb/paper-reading-notes)](https://github.com/zhangchangwei99-rgb/paper-reading-notes/releases)

面向学术研究者的中文论文精读 Skill。围绕研究问题、理论逻辑、数据与方法、主要结果及证据边界，产出一篇详细、可复查的中文读书笔记。读书笔记同时作为微信公众号等平台的发布稿，默认只交付一篇文章。

默认偏重经济、金融、会计与管理研究，其他学科按论文类型调整。采用理性、克制的学术语言，保留必要技术细节，不使用科普叙事、教学引导或宣传口吻，不对作者或论文作主观评价。

## 主要能力

- **研究逻辑**：梳理问题来源、文献脉络、理论关系与可检验预期。
- **方法分析**：展开测度构造、样本筛选、比较对象、估计对象和识别假设。
- **结果核对**：对照正文、表图和可访问附录，核对方向、数量级、单位、统计口径及不显著结果。
- **证据边界**：区分原文事实、作者解释和进一步讨论，说明因果识别与机制证据的适用条件。
- **统一成稿**：使用固定文章骨架，兼顾学术信息密度与公开平台排版。

## 安装

### 下载正式版本

从 [Releases](https://github.com/zhangchangwei99-rgb/paper-reading-notes/releases) 下载 `paper-reading-notes-v1.0.0.zip`，解压后将 `paper-reading-notes` 文件夹放入宿主的技能目录。

Codex 的用户技能目录为 `~/.agents/skills/`。最终结构应为：

```text
~/.agents/skills/paper-reading-notes/
├── SKILL.md
├── agents/
├── references/
└── scripts/
```

`SKILL.md` 应直接位于该目录下，避免多套一层同名目录。Codex 会自动检测技能变更；未显示时重启。目录约定参见 [官方技能文档](https://learn.chatgpt.com/docs/build-skills)。其他兼容宿主按其技能配置选择安装位置。

### 使用 Git

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/zhangchangwei99-rgb/paper-reading-notes.git "$HOME/.agents/skills/paper-reading-notes"
```

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/zhangchangwei99-rgb/paper-reading-notes.git ~/.agents/skills/paper-reading-notes
```

默认分支为当前维护版本，正式版本以 [版本标签](https://github.com/zhangchangwei99-rgb/paper-reading-notes/tags) 为准。

## 使用

提供论文 PDF、DOI 或原文链接，然后输入：

```text
使用 $paper-reading-notes 阅读附件论文，整理一篇详细中文读书笔记，兼作微信公众号发布稿。
```

需要调整重点时可补充：

```text
使用 $paper-reading-notes 阅读这篇论文，重点分析变量构造、识别策略、经济意义和机制证据。
```

默认交付一个 UTF-8 Markdown 文件；明确指定 Word、HTML 或聊天正文时，交付相应形式。同一文章不默认输出多种格式。内部核验记录、提取文本与渲染图片在成稿检查完成后清理，不另交底稿。

## 文章结构

1. 原文信息
2. 研究概述
3. 一、研究背景与核心问题
4. 二、相关文献与研究逻辑
5. 三、数据、变量与研究方法
6. 四、主要发现与证据
7. 五、稳健性与证据边界
8. 六、研究贡献与进一步讨论
9. 参考来源

标题陈述具体研究主题。二级内容随理论、实证、实验、调查或综述等论文类型调整；进一步讨论说明推论条件，不冒充原文结论。篇幅以充分解释关键研究环节为准。

## 运行条件与读取范围

本项目主要由指令、模板和相对路径参考文件组成，不内置模型、PDF 解析器、OCR 或发布接口，不依赖固定电脑路径。全文获取、PDF 读取和渲染由所在环境提供。

全文无法取得、扫描质量不足或附录不可访问时，成稿应说明实际读取范围。只有摘要时只能形成范围明确的初读概览，不能将其表述为完整精读。生成可供发布的文章不代表已经代发；操作外部平台需要用户明确授权和可用工具。

## 文件结构

```text
paper-reading-notes/
├── SKILL.md                    # 技能入口与核心工作规范
├── agents/openai.yaml          # 显示名称与默认调用提示
├── references/
│   ├── style-evidence.md        # 参考来源及编辑规则
│   ├── reading-protocol.md      # 精读与证据核验
│   ├── note-template.md         # 文章骨架
│   ├── publishing.md            # 单篇交付与发布边界
│   └── quality-gates.md         # 内容、数值和语言复核
├── scripts/validate_skill.py    # 无第三方依赖的结构检查
├── CHANGELOG.md
└── LICENSE
```

## 验证与维护

在仓库根目录运行结构检查，需要 Python 3.10 或更新版本，无第三方包依赖：

```text
python scripts/validate_skill.py
```

检查覆盖必要文件、UTF-8 编码、技能元数据、相对引用和本机路径泄漏。它不能验证论文分析的事实准确性；每次运行仍需对照原文复核内容与数值。

初版迭代覆盖文本网络方法、企业自然依赖测度、保护区政策分析和企业风险问卷四类样本。仓库保留归纳出的核验规则，不包含试跑文章或论文全文。抽样验证不保证未来每次输出无误。版本变更见 [CHANGELOG](CHANGELOG.md)；反馈问题可使用 [Issues](https://github.com/zhangchangwei99-rgb/paper-reading-notes/issues)，并提供可公开的原文定位和具体偏差。

## 许可证与参考来源

本项目的指令、模板、文档与脚本采用 [MIT License](LICENSE)。第三方论文、公众号文章和图表的权利归各自权利人所有，本项目的 MIT 许可不覆盖这些第三方材料。写作参考仅保留来源链接和编辑规则，见 [参考来源记录](references/style-evidence.md)。
