# 🎨 Hermes Skin Gallery

> 
>
> 67 套精心设计的终端皮肤，为 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 而生。
>
> 67 handcrafted terminal skins for [Hermes Agent](https://github.com/NousResearch/hermes-agent) — preview them all in your browser and apply with one click.

[![Skins](https://img.shields.io/badge/skins-67-brightgreen)](./skins/)
[![Dark](https://img.shields.io/badge/dark-49-blue)](./skins/)
[![Light](https://img.shields.io/badge/light-18-yellow)](./skins/)
| [![Website](https://img.shields.io/badge/preview-hermes--skins.top-blue)](https://www.hermes-skins.top)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
## 🖼 预览 / Preview

访问 [www.hermes-skins.top](https://www.hermes-skins.top) 即可看到所有 67 套皮肤的完整预览页面：
- 🎯 **真实终端模拟** — 每张卡片都是完整渲染的 Hermes CLI 界面
- 🎨 **实时配色对比** — 看到 prompt、边框、状态栏、响应区域的实际颜色
- 📋 **一键复制** — 点击任意皮肤的「复制 YAML 配置」按钮，粘贴即用
- 🔍 **筛选** — 支持全部 / 深色 / 浅色三种视图
<img width="761" height="860" alt="局部截取_20260603_100836" src="https://github.com/user-attachments/assets/3c9087c3-df18-44f6-81a2-486fd770f915" />


Open [www.hermes-skins.top](https://www.hermes-skins.top) in your browser to browse all 67 skins in a live preview:
- 🎯 **Real terminal mockups** — every card renders a complete Hermes CLI screen
- 🎨 **See the actual colors** — prompt, borders, status bar, response area
- 📋 **One-click copy** — click any skin's "Copy YAML" button
- 🔍 **Filter** — view all, dark-only, or light-only

## 📦 包含内容

```
hermes-skins-gallery/
├── README.md              ← 你在这里
├── LICENSE                 ← MIT
├── skins.json              ← 67 套皮肤元数据
├── preview/
│   └── index.html          ← 可视化预览页面
├── skins/                  ← 67 个可直接使用的 YAML 配置
│   ├── nebula.yaml
│   ├── midnight.yaml
│   ├── ... (65 more)
│   └── amber-glass.yaml
└── generate.py             ← (可选) 从 HTML 重新生成 YAML
```

## 🚀 快速使用

### 方法一：直接复制 YAML

在预览页面找到喜欢的皮肤，点击「复制 YAML 配置」，然后：

```bash
# 保存到 Hermes 的 skins 目录
# 把剪贴板内容粘贴保存为:
# ~/.hermes/skins/<皮肤名>.yaml

# 例如：
cat > ~/.hermes/skins/nebula.yaml
# 粘贴 YAML 内容，Ctrl+D 保存
```

然后在 Hermes CLI 中切换：

```
/skin nebula    # 即时切换！
```

### 方法二：批量安装

```bash
# 把所有 YAML 复制到 Hermes skins 目录
cp skins/*.yaml ~/.hermes/skins/

# 然后在 CLI 里用 /skin 切换
```

## 🌙 深色主题 (49 套)

### 基础系列
`nebula` `midnight` `matrix` `dracula` `ember` `synthwave` `nord` `tokyo-night` `catppuccin` `onedark` `gruvbox-dark` `monokai` `oceanic` `vampire` `cyberpunk` `forest` `ink` `bloodmoon` `arctic` `royal` `carbon` `rust`

### 特殊概念系列
`retro-amber` `retro-green` `tron` `hologram` `aurora` `plasma` `vaporwave` `wasteland` `oled` `thermal` `starlight` `neon-noir` `sakura-night` `matcha` `rosepine` `everforest` `blueprint` `chalkboard` `steampunk` `underwater` `campfire` `desert-night` `brew` `gemstone` `coral-reef` `storm` `carbon-fiber`

## ☀ 浅色主题 (18 套)

`frost` `sepia` `blossom` `solarized` `latte` `gruvbox-light` `nord-light` `vanilla` `lavender` `mint` `peachy` `sky` `rosey` `bamboo` `autumn` `polaroid` `snowfield` `amber-glass`

## 🎨 皮肤设计理念

每套皮肤不只是换个颜色——每套都有一个**完整的概念**：

| 皮肤 | 概念 | 灵感 |
|------|------|------|
| **Retro Amber** | 单色 CRT 终端 | VT100 琥珀荧光粉 |
| **Retro Green** | IBM 3270 | P1 绿色荧光粉 |
| **Tron** | 创战纪 | 电影光栅风格 |
| **Hologram** | 全息彩虹 | 多色全息贴纸 |
| **OLED** | 纯黑省电 | OLED 屏幕物理特性 |
| **Thermal** | 热成像仪 | 蓝→紫→红→黄渐变 |
| **Vaporwave** | 蒸汽波 | A E S T H E T I C |
| **Wasteland** | 废土 | Fallout 后启示录 |
| **Blueprint** | CAD 蓝图 | 工程设计图纸 |
| **Chalkboard** | 黑板粉笔 | 课堂记忆 |
| **Steampunk** | 蒸汽朋克 | 维多利亚工业 |
| **Underwater** | 深海 | 6000 米海底 |

每套皮肤的 `thinking_verbs`（思考动词）、`waiting_faces`（等待表情）、`prompt_symbol`（提示符）和 `welcome 消息`都经过定制，与概念主题保持一致。

## 🛠 YAML 结构说明

```yaml
name: nebula                          # 皮肤标识符
description: "星云紫 · 霓虹青"       # 简短描述
colors:                               # 16 个颜色位
  banner_border: "#7c4dff"            # 横幅边框
  banner_title: "#b388ff"             # 横幅标题
  banner_accent: "#00e5ff"            # 横幅强调
  # ... (更多颜色位)
spinner:
  waiting_faces: ["(◉)","(◎)","(◈)"] # 等待中的表情动画
  thinking_verbs: ["计算中","思考中"] # 思考时的动词
branding:
  agent_name: "✦ 星云"               # Agent 显示名称
  welcome: "星云引擎已启动"           # 欢迎消息
  prompt_symbol: "✦"                  # 提示符
  response_label: "星云"              # 响应标签
tool_prefix: "┊"                      # 工具输出前缀
```

## 📋 自定义皮肤

你可以基于这些模板创建自己的皮肤：

```bash
# 复制一个现成的
cp skins/nebula.yaml ~/.hermes/skins/my-theme.yaml

# 编辑配色
vim ~/.hermes/skins/my-theme.yaml

# 切换
/skin my-theme
```

详细文档: [Hermes Skin System](https://github.com/NousResearch/hermes-agent)

## 📄 许可

MIT License — 自由使用、修改、分发。

## 🙏 致谢

- [Nous Research](https://nousresearch.com) — Hermes Agent 项目
- 所有经典编辑器和终端主题的灵感来源（Dracula, Nord, Catppuccin, Gruvbox, One Dark, Monokai, Solarized, Rose Pine, Everforest）

---

⭐ 如果这个皮肤包对你有用，欢迎 Star 和分享！
