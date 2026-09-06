# 独立 MD：版本与更新 / Standalone MD versions

## 给使用者

- 不支持项目安装的 Agent，直接接收首页“方式二”的在线 MD 链接即可；不需要先读取首页、安装 ZIP 或打开其他规范文件。
- **在线 MD** 使用明确版本路径。首页会在发布新版时更新链接；已经复制出去的旧版本链接仍指向旧版，不会自动升级。
- **最新发布版下载** 使用 `releases/latest/download/` 固定入口，随 GitHub 最新正式 Release 切换。下载后作为附件上传，也可复制全文。
- **`main` 文件** 是开发中的源文件，不作为面向 Agent 的首选发布入口。
- **已添加的技能** 是保存到宿主里的内容，不会自动跟随 GitHub 更新。更新时需要重新读取新 MD，并按宿主能力更新或重新添加技能。

GitHub 入口更新不等于第三方缓存立即失效。若 Agent 仍读到旧内容或读不全，请使用下载的 MD 附件，不让它凭印象执行。直接浏览或下载文件也不等于已经安装技能。

当前发布入口和两个即梦使用示例见 [中文首页方式二](../README.md#方式二把-md-当作完整提示词直接使用)。`v1.3.0` 绘图规范仍保持原样；四张候选由首页使用提示词明确指定，本次入口维护没有修改绘图规范。

## 发布维护

1. 先完成目标 Agent 测试，更新 `VERSION` 和正式绘图文件。
2. 将中英文 README、安装指南及使用示例中的版本链接一并更新到待发布版本；运行 `python tools/release_prompts.py`。版本不一致或入口退回普通相对路径时，仓库 CI 会失败。
3. 提交并创建对应正式 tag。**不要移动旧 tag、改写旧版本内容或清空 Git 历史。**
4. 发布对应 Release（新版本应设为 Latest）。`Publish standalone prompt MDs` 工作流会从该 tag 导出并上传两个独立 MD 和 `prompt-release.json`，不把工作区里的其他版本误传进去。
5. 如果自动发布未运行，可在 Actions 手动运行该工作流并指定 tag，或执行下方命令。既有附件不自动覆盖；重跑遇到同名附件时先检查其哈希，不使用 `--clobber` 掩盖版本错误。
6. 发布完成后核验：Release 的 tag、首页在线链接、最新下载重定向目标、两个 MD 的 SHA-256 与 `prompt-release.json` 一致。下载附件上传完成前，不宣称新入口已经可用。

```bash
python tools/validate_repo.py
python -m unittest discover -s tools -p "test_*.py"
python tools/release_prompts.py --tag vMAJOR.MINOR.PATCH
gh release upload vMAJOR.MINOR.PATCH dist/prompts/photo-poetic-postcard-prompt.zh-CN.md dist/prompts/photo-poetic-postcard-prompt.en.md dist/prompts/prompt-release.json
```

`vMAJOR.MINOR.PATCH` 需替换为实际正式 tag。在线文件和附件内容相同，不另维护一套缩短版提示词。版本和哈希放在发布清单中，不混入绘图指令。

## English

Send the standalone MD link directly to an Agent; repository installation is not required. The homepage's online links pin a specific release. Previously copied links remain pinned, so revisit the homepage to update. The stable download links follow GitHub's latest Release, but no URL can force a third-party reader to invalidate its cache. Attach the downloaded MD if URL reading is stale or incomplete. Previously saved host skills do not automatically update.

For maintainers: update `VERSION` and all public versioned entry links together. CI checks their consistency. On a stable Release, the publishing workflow exports the exact tagged Markdown, plus a tag/commit/SHA-256 manifest. It refuses to overwrite existing release assets. Verify both online links and downloaded bytes after publication. The entry-point maintenance preserves the v1.3.0 drawing files; the four-candidate examples are explicit user overrides, not a rewritten guide.

GitHub 官方下载链接格式：[Linking to releases](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases)。
