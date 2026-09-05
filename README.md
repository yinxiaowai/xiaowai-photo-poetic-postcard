## 作者介绍

作者：AI尹小歪

中国美术学院AI中心特聘讲师  
WaytoAGI 认证讲师 & 视频学社主理人 & AI工具测评专家  
资深AIGC实战创作者、企业AI培训讲师

赛博吉他歌手

🔯为你挖掘各种AI效率工具  
📘保姆级教程带你拆解AI工具热门玩法

欢迎关注我的两个内容入口：公众号看完整图文拆解，视频号看工具实测与案例演示。

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <strong>微信公众号｜小歪的AI工具箱</strong><br>
      AI 资讯、保姆级教程与完整图文拆解<br><br>
      <a href="assets/images/wechat-qr.png"><img src="assets/images/wechat-qr.png" width="314" alt="小歪的AI工具箱公众号二维码"></a>
    </td>
    <td align="center" valign="top" width="50%">
      <strong>视频号｜AI尹小歪</strong><br>
      AI 工具实测、案例演示与视频教程<br><br>
      <a href="assets/images/wechat-channels-qr.jpg"><img src="assets/images/wechat-channels-qr.jpg" width="220" alt="AI尹小歪视频号二维码"></a>
    </td>
  </tr>
</table>

我的个人专栏：https://waytoagi.feishu.cn/wiki/Pddywh6NqiRKb4kaJBscAbf9nUA

---

![Photo Poetic Postcard](assets/images/banner.svg)

# Photo Poetic Postcard｜照片诗意明信片 Skill

[English](README_EN.md)

![Agent Skill](https://img.shields.io/badge/Agent-Skill-C46A32?style=flat-square)
![One Photo One Result](https://img.shields.io/badge/One%20Photo-One%20Result-D97706?style=flat-square)
![Model Adaptive](https://img.shields.io/badge/Model-Adaptive-A16207?style=flat-square)
![Content License](https://img.shields.io/badge/Content-CC%20BY--NC--SA%204.0-2F2A25?style=flat-square)

把一张用户照片制作成一张完整的诗意明信片：上方保留原摄影，下方只提取其中一个主元素进行艺术转绘，并配以克制的标题、短注与取色色卡。

这不是绑定某一个模型的提示词，也不要求一次生成多张候选。它是一套可安装、可直接复制、可降级运行、可二次定义的跨 Agent 工作流。

## 效果图展示

以下均为授权原图在一次完整生图操作中得到的实测成品，不是先生成下半图再拼接，也没有事后用程序添加文字。六张成品均已核验为 `1086 × 1448`，精确 3:4。点击每张下方的“查看原图”可对照内容提取方式；完整案例记录见 [examples/README.md](examples/README.md)。

<!-- GALLERY:START -->
<table>
  <tr>
    <td width="33%" align="center"><img src="examples/gallery/results/case-01-xiaoqikong-result.webp" alt="小七孔照片诗意明信片效果图"><br><strong>01 · 小七孔</strong><br><a href="examples/gallery/sources/case-01-xiaoqikong-source.webp">查看原图</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-02-shaolin-result.webp" alt="少林寺照片诗意明信片效果图"><br><strong>02 · 少林寺</strong><br><a href="examples/gallery/sources/case-02-shaolin-source.webp">查看原图</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-03-kitten-result.webp" alt="小猫照片诗意明信片效果图"><br><strong>03 · 玉米旁的小猫</strong><br><a href="examples/gallery/sources/case-03-kitten-source.webp">查看原图</a></td>
  </tr>
  <tr>
    <td width="33%" align="center"><img src="examples/gallery/results/case-04-golden-hall-result.webp" alt="金殿照片诗意明信片效果图"><br><strong>04 · 金殿</strong><br><a href="examples/gallery/sources/case-04-golden-hall-source.webp">查看原图</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-05-portrait-result.webp" alt="人物照片诗意明信片效果图"><br><strong>05 · 水上人物</strong><br><a href="examples/gallery/sources/case-05-portrait-source.webp">查看原图</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-06-riverside-result.webp" alt="水岸游船照片诗意明信片效果图"><br><strong>06 · 水岸游船</strong><br><a href="examples/gallery/sources/case-06-riverside-source.webp">查看原图</a></td>
  </tr>
</table>
<!-- GALLERY:END -->

## 它解决了什么

- 一张原图只交付一张最终成品，不生成四张候选或四宫格。
- 不把下半区做成整幅照片的水彩复刻，只转绘一个主元素。
- 采用“拆解 → 选择性保留 → 蒸馏 → 重构”：只保留主体和零至三个直接相连的辨识线索，明确删除可识别的完整背景。
- 不写死 Image Gen、即梦、豆包或其他模型，根据当前 Agent 的真实能力选择执行方式。
- 有生图能力时直接生成；没有生图能力时输出一条已经分析并填好的完整提示词。
- Agent 无法安装 Skill 时，可直接使用独立的中英文 Prompt MD。
- 先判断地点证据；已确认的地点或景点名称必须进入标题或短注，无法确认时才使用场景文案且不猜地名。
- 用户可调整尺寸、比例、转绘风格、排版、文字、纸张、色卡与配色倾向。
- 上方照片、下方转绘、纸张、文字、色卡与排版必须在同一次生图中完整生成，不允许后期拼接或程序排字。

## 能力与平台兼容

| 平台 / 场景 | 推荐方式 | 能否直接生图 | 说明 |
| --- | --- | --- | --- |
| Codex / ChatGPT 桌面端 | 安装标准 Skill | 取决于当前会话是否有图片理解与生成工具 | 有工具就生成；无工具则输出可复制提示词 |
| Claude Code | 复制到个人或项目 Skills 目录 | 取决于已接入的模型、MCP 或图片工具 | Skill 本身不强制指定供应商 |
| WorkBuddy | 上传专用 ZIP | 取决于工作区选择的模型或连接器 | 提供符合 WorkBuddy 元数据要求的发行包 |
| Gemini CLI | 从 Git 仓库安装 | 取决于当前工具配置 | 支持标准 Agent Skills 目录 |
| 其他支持 `SKILL.md` 的 Agent | 安装标准 Skill 或手动复制 | 取决于宿主能力 | 遵循开放 Agent Skills 基本结构 |
| 即梦 / 豆包等自带生图 Agent | 直接使用 Prompt MD | 通常可在产品内完成 | 暂不宣称支持 GitHub Skill 安装 |
| 普通生图工具 | 上传原图并复制完整提示词 | 是 | 若工具不能先分析图片，先让视觉 Agent 填好主体和颜色 |

> “Skill 可安装”和“宿主有生图模型”是两件事。本项目只规定工作流，不伪装宿主不存在的能力。

更详细的平台说明见 [安装与兼容指南](docs/INSTALLATION.md)。

## 使用方法

### 方式一：作为 Agent Skill 安装

#### Codex

在 Codex 中对 `$skill-installer` 说：

```text
请从 https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard 安装这个 Skill。
```

也可手动克隆到用户 Skills 目录：

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.agents/skills/xiaowai-photo-poetic-postcard
```

#### Claude Code

个人级安装：

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.claude/skills/xiaowai-photo-poetic-postcard
```

项目级安装时，把目录放进：

```text
.claude/skills/xiaowai-photo-poetic-postcard/
```

#### Gemini CLI

```bash
gemini skills install https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git --consent
```

#### WorkBuddy

从 GitHub Releases 下载 `xiaowai-photo-poetic-postcard-workbuddy.zip`，在 WorkBuddy 的 Skill 创建/上传入口导入。该包使用 `skills/xiaowai-photo-poetic-postcard/SKILL.md` 结构，并包含 WorkBuddy 要求的双语描述、版本与作者元数据。

安装后，上传一张照片并直接说：

```text
使用 xiaowai-photo-poetic-postcard 把这张照片制作成一张诗意明信片。
```

如果想微调：

```text
使用 xiaowai-photo-poetic-postcard，把这张照片制作成 4:5 竖版明信片。上方照片占 60%，下方改成淡墨加彩铅，不要色卡，标题写“海风经过”。最终只给我一张图。
```

### 方式二：把 MD 当作完整提示词直接使用

Agent 安装不了 Skill 时，上传照片并粘贴下面任一文件的完整内容：

| 语言 | 文件 |
| --- | --- |
| 中文 | [references/photo-poetic-postcard-prompt.zh-CN.md](references/photo-poetic-postcard-prompt.zh-CN.md) |
| English | [references/photo-poetic-postcard-prompt.en.md](references/photo-poetic-postcard-prompt.en.md) |

这也是即梦 Agent、豆包 Agent 或其他带生图能力但不支持 GitHub Skill 安装的平台的推荐方式。

想确认“完整文件”最终应被解析成什么样，可以查看 [荔波小七孔已编译提示词示例](references/example-xiaoqikong-compiled-prompt.zh-CN.md)。示例只演示结构，不能把其中的地点、主体、颜色或文案套到其他照片。

> **不要只复制其中一小段，也不要让中间 Agent 把它“总结成更简洁的提示词”。** 完整 MD 会要求 Agent 在调用生图模型前明确写出具体主体、具体删除清单、标题、短注、三个颜色及版式位置，并保留全部上下分区约束。若最终送入图片模型的只是一段“上面保留照片、下面把同一场景水彩重绘”的概括，说明提示词交接失败，应停止生成并重新使用完整文件。

## 为什么这一版在不同 Agent 中更稳

参考项目的有效做法，是把可直接使用的 Prompt MD 写成从输入分析到输出限制的完整执行规范，而不是只提供风格关键词。本项目在此基础上加入更严格的下游提示词协议：

1. 默认整张 3:4 画布严格分成上下各 50% 的两个独立区域。
2. 主 Skill 内直接内嵌完整中文生图模板，不依赖 Agent 一定会继续读取引用文件。
3. Agent 必须先把“一个具体主体”和“本图具体删除清单”写进最终提示词；“整幅风景”或“同一场景”不能充当主体。
4. 最终提示词必须保留五个分区，禁止概括、缩写或改写成一段普通描述。
5. 三枚色卡被写成可检查的数字规则：每枚边长约为下半区宽度 `1/20`，等大、纯色、完美正方形。
6. 缺少任一分区、主体、删除清单、准确文案、三个颜色或交付限制时，Agent 不得开始生图。

## 三种运行结果

| 当前 Agent 的能力 | Skill 的行为 |
| --- | --- |
| 能看图 + 能生图 | 直接生成并交付一张最终图 |
| 能看图 + 不能生图 | 分析原图，返回一条已填好的完整生图提示词，不假装已生成 |
| 不能看图 | 明确说明缺少图片理解能力，不编造主体、颜色、地点或构图 |

无论 Agent 是否能够运行本地代码，都不得把成品拆成“下半区生图 + 本地拼接”。本项目要求模型一次生成完整构图；本地代码只负责仓库校验与发行包构建，不参与视觉成品制作。

## 可自由调整的部分

| 参数 | 默认 | 可以怎么改 |
| --- | --- | --- |
| 画布 | 3:4，1080×1440 | 4:5、1:1、9:16 或自定义像素 |
| 上下占比 | 严格各 50% | 用户可明确调整约 40%–65%；Agent 不得自行漂移；照片铺满顶部和左右边缘 |
| 转绘媒介 | 透明水彩 + 轻水粉 + 彩铅 | 水墨、版画、拼贴纸感、克制数字绘画等 |
| 主体尺度 | 中等偏小、随复杂度自适应 | 横向/复杂主体约占下方宽度 55%–70%；人物、动物、圆环等约 40%–55% |
| 主体位置 | 根据轮廓与负空间决定 | 可偏左、居中或偏右；至少保留约 45% 连续干净纸面 |
| 纸张 | 暖米白纤维纸 | 冷灰白、手工纸、平滑美术纸 |
| 文字 | 中文标题 + 短注 | 自定义文案、语言、字体，或完全去掉 |
| 色卡 | 三枚，在下半区四角中择空位成组放置 | 调整位置或隐藏；显示时仍是三枚纯色正方形，每枚边长约为下半区宽度 1/20 |
| 色彩 | 从原图取色、低饱和 | 更暖、更冷、单色强调，但仍可追溯到原图 |
| 排版 | 先排主体，再根据负空间放文字与色卡 | 两组可在下半区四角间变化，尽量分处不同角落，不遮挡主体 |

## 不建议改掉的核心原则

1. 原图始终是唯一内容来源，上半区照片不应被语义重画、扩展或补造。
2. 下半区只提取并转绘一个主元素，不把整幅原图重新画一遍。
3. 最终是一张完整作品，不输出候选合集。
4. 地点判断顺序为“用户明确提供 > 清晰招牌/EXIF/定位 > 高置信度唯一地标”；确认后必须在标题或短注中原样出现，不能确认时不猜地名。
5. 默认让上方照片铺满其区域，不留纸边、不加描边；比例不同时只做必要裁切，不拉伸、不扩图。
6. 默认输出必须通过真实像素比例检查；3:4 作品出现 2:3 尺寸时必须在生图阶段修复。

## 项目结构

```text
xiaowai-photo-poetic-postcard/
├── SKILL.md                         # 跨 Agent 主 Skill
├── agents/openai.yaml               # Codex / ChatGPT 展示信息
├── references/
│   ├── postcard-design.md           # 视觉系统、变量与失败修复
│   ├── photo-poetic-postcard-prompt.zh-CN.md
│   └── photo-poetic-postcard-prompt.en.md
├── tools/
│   ├── build_packages.py            # 构建标准版与 WorkBuddy ZIP
│   └── validate_repo.py             # 仓库检查
├── examples/                        # 经授权的原图与效果图
├── README.md
└── README_EN.md
```

## 构建与验证

```bash
python tools/validate_repo.py
python tools/build_packages.py
```

发行时会生成：

- `dist/xiaowai-photo-poetic-postcard-standard.zip`
- `dist/xiaowai-photo-poetic-postcard-workbuddy.zip`

## 许可证

本项目采用清晰的分层许可：

- `SKILL.md`、提示词、视觉规范、README 和其他文字内容：**CC BY-NC-SA 4.0**。允许署名、非商业使用、修改与分享；衍生内容需采用相同许可。商业使用请先取得作者授权。
- `tools/` 中的代码：**MIT License**。
- `assets/images/wechat-qr.png`、`assets/images/wechat-channels-qr.jpg`、作者身份素材，以及 `examples/` 中的用户原图和效果图：**不包含在上述开放许可中**，仅用于项目介绍与效果展示，除非对应文件另有说明。

完整范围见 [LICENSE](LICENSE)、[LICENSE-CODE](LICENSE-CODE) 与 [NOTICE.md](NOTICE.md)。因为核心提示词带有“非商业”限制，本项目更准确地说是“开放共享”；其中 MIT 代码部分属于标准开源软件。

## 致谢与反馈

如果你用它做出了喜欢的作品，欢迎在 GitHub Discussions 或 Issues 分享使用平台、参数与结果。提交公开案例前，请确认你拥有原图和人物肖像的必要授权。
