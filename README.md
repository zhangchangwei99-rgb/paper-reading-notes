# Paper Reading Notes · 学术文献研读与笔记

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/zhangchangwei99-rgb/paper-reading-notes)](https://github.com/zhangchangwei99-rgb/paper-reading-notes/releases)

面向学术研究者的中文论文精读 Skill。围绕研究问题、理论逻辑、数据与方法、主要结果及证据边界，产出一篇精练、可复查的中文读书笔记。读书笔记同时作为微信公众号等平台的发布稿，默认只交付一个 Word 文档。

默认偏重经济、金融、会计与管理研究，其他学科按论文类型调整。采用理性、克制的学术语言，保留必要技术细节，不使用科普叙事、教学引导或宣传口吻，不对作者或论文作主观评价。

## 主要能力

- **研究逻辑**：梳理问题来源、文献脉络、理论关系与可检验预期。
- **方法分析**：展开测度构造、样本筛选、比较对象、估计对象和识别假设。
- **结果核对**：对照正文、表图和可访问附录，核对方向、数量级、单位、统计口径及不显著结果。
- **证据边界**：区分原文事实、作者解释和进一步讨论，说明因果识别与机制证据的适用条件。
- **图文分析**：必要时截取原论文关键图表嵌入 Word，围绕研究发现解释经济含义，避免逐行逐列报数。
- **统一成稿**：固定文章主线，保留关键方法与证据，删去重复解释；正文通常约3,000—4,000中文字符。

## 安装

### 下载技能包

下载 [当前维护版 ZIP](https://github.com/zhangchangwei99-rgb/paper-reading-notes/archive/refs/heads/main.zip)，或在 [Releases](https://github.com/zhangchangwei99-rgb/paper-reading-notes/releases) 选择所需版本。解压后将包含 `SKILL.md` 的目录命名为 `paper-reading-notes`，放入宿主的技能目录。当前维护版包含最新的格式和写作规则，旧版发布包保留对应版本行为。

Codex 的用户技能目录为 `~/.agents/skills/`。最终结构应为：

```text
~/.agents/skills/paper-reading-notes/
├── SKILL.md
├── agents/
├── references/
└── scripts/
```

`SKILL.md` 应直接位于该目录下，避免多套一层同名目录。安装后在宿主中确认技能已被识别；必要时重新加载或重启。其他兼容宿主按其技能配置选择安装位置。

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

默认只交付一个 `.docx` Word 文件。正文不含公式、自制表格、研读版本／覆盖清单或文末参考来源；必要时嵌入原论文的关键图表截图，保留原编号、关键表头和注释，并在正文解释发现与经济含义，不逐项罗列读数。原表截图允许保留原有符号，不允许公式截图。

明确指定其他格式时遵循，同一文章不默认输出多种格式。Python 脚本只是内部工具，不作为笔记交付。核验记录、提取文本、截图及渲染页在成稿检查完成后清理；文档图片完整内嵌，不依赖临时文件。

## 文章结构

1. 原文信息
2. 研究概述
3. 一、研究背景与核心问题
4. 二、相关文献与研究逻辑
5. 三、数据、变量与研究方法
6. 四、主要发现与证据
7. 五、稳健性与证据边界
8. 六、研究贡献与讨论

标题陈述具体研究主题。二级内容随理论、实证、实验、调查或综述等论文类型调整；进一步讨论说明推论条件，不冒充原文结论。默认约3,000—4,000中文字符，复杂方法可适当增加。背景服务于设计，方法保留核心链条，结果围绕发现推进；定义、结果和限制避免重复。

## 运行条件与读取范围

本项目主要由指令、模板和相对路径参考文件组成，不内置模型、PDF 解析器、OCR 或发布接口，不依赖固定电脑路径。全文获取、PDF 读取和渲染由所在环境提供。

Word 制作与渲染需要宿主具备相应文档能力，脚本不内置文档生成器。全文无法取得或关键内容无法核实时，如实说明限制；只有摘要时不能声称完成精读。版本和阅读覆盖记录留在内部，影响结论的缺口在相应分析处简述，不另列覆盖清单。生成可供发布的文章不代表已经代发；操作外部平台需要用户明确授权和可用工具。

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
├── scripts/
│   ├── validate_skill.py        # 无第三方依赖的结构检查
│   └── validate_note.py         # Word禁项及图片内嵌检查
├── CHANGELOG.md
└── LICENSE
```

## 验证与维护

在仓库根目录运行结构检查，需要 Python 3.10 或更新版本，无第三方包依赖：

```text
python scripts/validate_skill.py
```

检查覆盖必要文件、UTF-8 编码、技能元数据、相对引用和本机路径泄漏。另可检查默认 Word 成稿：

```text
python scripts/validate_note.py "论文简称-读书笔记.docx"
```

文档检查排查自制表格、公式对象／常见符号写法、禁用栏目、残留 Markdown 及未内嵌图片。两个脚本都不能验证学术事实、分析质量或图片清晰度；每次运行仍须对照原文复核，并渲染逐页查看。

初版迭代覆盖文本网络方法、企业自然依赖测度、保护区政策分析和企业风险问卷四类样本。本次更新另对照用户指定的内幕交易笔记与原论文重点证据，形成精练取舍、图表解读及构念口径核验规则。仓库不包含试跑文章、论文全文或第三方截图。抽样校验不保证未来每次输出无误。版本变更见 [CHANGELOG](CHANGELOG.md)；反馈问题可使用 [Issues](https://github.com/zhangchangwei99-rgb/paper-reading-notes/issues)，并提供可公开的原文定位和具体偏差。

## 许可证与参考来源

本项目的指令、模板、文档与脚本采用 [MIT License](LICENSE)。第三方论文、公众号文章和图表的权利归各自权利人所有，本项目的 MIT 许可不覆盖这些第三方材料。写作参考仅保留来源链接和编辑规则，见 [参考来源记录](references/style-evidence.md)。
