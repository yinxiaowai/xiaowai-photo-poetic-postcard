# 安装与兼容指南

## 安装前先理解两层能力

本项目把“读取工作流”和“生成图片”分开处理：

1. **Skill 层**：Agent 能否发现并读取 `SKILL.md`。
2. **图片层**：当前会话是否有图片理解、参考图生图/编辑、文件输出能力。

成功安装 Skill 不代表宿主一定有生图模型；没有原生生图工具也不代表 Skill 完全不可用。只要 Agent 能看图，它仍可输出一条针对原图填好的完整提示词。

## 标准 Agent Skills 包

标准包遵循 `skill-name/SKILL.md` 的基本结构，可供支持 Agent Skills 的宿主使用。

### Codex

官方当前的用户级目录是 `$HOME/.agents/skills`，仓库级目录是 `.agents/skills`。推荐让内置 `$skill-installer` 从 GitHub 安装；也可手动克隆。

PowerShell：

```powershell
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git "$env:USERPROFILE\.agents\skills\xiaowai-photo-poetic-postcard"
```

macOS / Linux：

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.agents/skills/xiaowai-photo-poetic-postcard
```

如果没有出现，重启 Codex 或让它重新扫描 Skills。

官方说明：[OpenAI — Build skills](https://developers.openai.com/codex/skills/)

### Claude Code

用户级目录：

```text
~/.claude/skills/xiaowai-photo-poetic-postcard/SKILL.md
```

项目级目录：

```text
.claude/skills/xiaowai-photo-poetic-postcard/SKILL.md
```

PowerShell 用户级安装：

```powershell
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git "$env:USERPROFILE\.claude\skills\xiaowai-photo-poetic-postcard"
```

官方说明：[Anthropic — Extend Claude with skills](https://code.claude.com/docs/en/skills)

> Claude Code 能读取 Skill，但是否能直接生成图片取决于你为它接入的模型、MCP、CLI 或其他图片工具。没有图片工具时会进入提示词交接路径。

### Gemini CLI

```bash
gemini skills install https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git --consent
```

也可以放进用户级 `~/.gemini/skills/`、`~/.agents/skills/`，或项目级 `.gemini/skills/`、`.agents/skills/`。

官方说明：[Gemini CLI — Agent Skills](https://geminicli.com/docs/cli/skills/)

### 其他 Agent

如果宿主支持开放 Agent Skills 结构，把标准发行包解压到它规定的 Skills 目录。至少应保持：

```text
xiaowai-photo-poetic-postcard/
├── SKILL.md
└── references/
```

规范参考：[Agent Skills Specification](https://agentskills.io/specification)

## WorkBuddy 专用包

WorkBuddy 要求压缩包内部以 `skills/{skill-name}/SKILL.md` 组织，并要求版本、作者和中英文描述等额外元数据。它与最小化的通用 Agent Skills frontmatter 不完全相同，因此本项目单独构建兼容包，而不是把平台私有字段塞进通用 `SKILL.md`。

1. 打开 GitHub Releases。
2. 下载 `xiaowai-photo-poetic-postcard-workbuddy.zip`。
3. 在 WorkBuddy 的 Skills 页面选择新增/创建 Skill 并上传 ZIP。
4. 解析成功后，在预览会话中上传照片测试。
5. 若工作区模型没有图片生成能力，应得到完整提示词，而不是虚假的图片完成状态。

官方说明：[WorkBuddy 开放平台 — Skill](https://open.workbuddy.cn/docs/skill)

## 即梦与豆包

无需把项目首页交给 Agent，也不要求支持 GitHub 仓库安装。推荐直接读取独立 MD：

1. 打开具备图片理解与生成能力的 Agent/创作入口。
2. 上传一张原图。
3. 发送 [当前发布版中文 MD · v1.3.0](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/blob/v1.3.0/references/photo-poetic-postcard-prompt.zh-CN.md) 链接；无法读取时，[下载最新发布版 MD](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/releases/latest/download/photo-poetic-postcard-prompt.zh-CN.md) 后上传附件，或复制全文。
4. 用自然语言补充想调整的尺寸、比例、风格或文字；没有额外要求时直接执行。
5. v1.3.0 默认一张完整成品；明确要求四张时，输出四张独立候选，不合成四宫格。

即梦的“只生图”和“生图后添加技能”两段使用提示词见 [首页方式二](../README.md#方式二把-md-当作完整提示词直接使用)，用户已反馈测试通过。“添加技能”指即梦内创建可复用技能卡片并由用户确认，不等于从任意 GitHub 仓库安装；其他 Agent 是否支持要以其实际能力为准。已保存的技能不会因仓库更新而自动同步。[版本与更新说明](PROMPT_VERSIONS.md)

该 MD 本身含完整观察和绘图方法，不需要填写模板或另读项目文件。Agent 根据照片决定主体、取舍与布局，再把具体决定及生效规则传给图片模型。

## 普通生图工具

如果工具支持参考图但不支持多轮 Agent 分析：

1. 若工具能同时理解参考图和长文本，可直接上传原图并粘贴绘图规范全文。
2. 若不能完成其中的观察与取舍，让视觉 Agent 根据这份独立规范和原图作出具体决定，并输出完整生图指令。
3. 上传同一张原图到生图工具并使用该具体指令；保留全部适用的上下分区、主体删除清单、文案规则。

如果工具完全不支持参考图，这个 Skill 无法可靠保证原图忠实与主元素溯源，不建议声称完成了该工作流。

## 安全与隐私

- 安装第三方 Skill 前先阅读 `SKILL.md` 与它引用的文件。
- 本项目的 Python 工具只用于校验与打包，不参与明信片图像的生成、拼接或排字。
- 上传含人物、儿童、住址、证件或私人场景的照片前，先确认所用平台的隐私政策与授权范围。
- 公开效果图前，确认原图版权和肖像授权。
