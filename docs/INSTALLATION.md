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

本项目目前没有找到它们支持从任意 GitHub 仓库安装 `SKILL.md` 的官方依据，因此不把“可安装”写成已验证能力。推荐流程：

1. 打开具备图片理解与生成能力的 Agent/创作入口。
2. 上传一张原图。
3. 粘贴 [中文 Prompt MD](../references/photo-poetic-postcard-prompt.zh-CN.md) 的完整指令代码块。
4. 在开头填写想调整的尺寸、比例、风格和文字。
5. 只保留一张最终结果；多图网格视为不合格输出。

## 普通生图工具

如果工具支持参考图但不支持多轮 Agent 分析：

1. 先用视觉 Agent 分析原图，得到一个主元素、最多两个伴随线索、三种颜色、标题和短注。
2. 把这些值填入 Prompt MD。
3. 上传同一张原图到生图工具并粘贴具体化后的提示词。

如果工具完全不支持参考图，这个 Skill 无法可靠保证原图忠实与主元素溯源，不建议声称完成了该工作流。

## 安全与隐私

- 安装第三方 Skill 前先阅读 `SKILL.md` 与它引用的文件。
- 本项目的 Python 工具只用于校验与打包，不参与明信片图像的生成、拼接或排字。
- 上传含人物、儿童、住址、证件或私人场景的照片前，先确认所用平台的隐私政策与授权范围。
- 公开效果图前，确认原图版权和肖像授权。
