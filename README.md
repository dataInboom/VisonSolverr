# FlareSolverr

[![Latest release](https://img.shields.io/github/v/release/FlareSolverr/FlareSolverr)](https://github.com/FlareSolverr/FlareSolverr/releases)
[![Docker Pulls](https://img.shields.io/docker/pulls/flaresolverr/flaresolverr)](https://hub.docker.com/r/flaresolverr/flaresolverr)
[![Docker Stars](https://img.shields.io/docker/stars/flaresolverr/flaresolverr)](https://hub.docker.com/r/flaresolverr/flaresolverr)
[![GitHub issues](https://img.shields.io/github/issues/FlareSolverr/FlareSolverr)](https://github.com/FlareSolverr/FlareSolverr/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/FlareSolverr/FlareSolverr)](https://github.com/FlareSolverr/FlareSolverr/pulls)
[![GitHub Repo stars](https://img.shields.io/github/stars/FlareSolverr/FlareSolverr)](https://github.com/FlareSolverr/FlareSolverr)

## About This Project / 关于本项目

This project is based on the open source [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr).
A new API endpoint `request.vision` has been added to extract visual feature information of page elements.

本项目基于开源的 [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) 项目。
新增了获取页面视觉信息特征的接口，你可以通过 `request.vision` 命令快速获取页面上所有可见标签的视觉特征。

## Vision API / 视觉接口

The `request.vision` command works similarly to `request.get`, but additionally returns a `vision` field containing visual feature data (position, size, font, XPath, etc.) for every DOM element on the page.

`request.vision` 命令与 `request.get` 的用法类似，但返回结果中会额外包含一个 `vision` 字段，包含页面上每个 DOM 元素的视觉特征数据（位置、尺寸、字体、XPath 等）。

### Python Example

```python
import requests

response = requests.post(
    'http://127.0.0.1:8191/v1',
    json={
        'cmd': 'request.vision',
        'url': url,
        'maxTimeout': 60000
    },
    headers={'Content-Type': 'application/json'}
)
result = response.json()
vision = result.get('solution', {}).get('vision')
```

### cURL Example

```bash
curl -X POST http://127.0.0.1:8191/v1 \
  -H 'Content-Type: application/json' \
  -d '{"cmd": "request.vision", "url": "https://example.com", "maxTimeout": 60000}'
```

You can use the visual feature data to quickly extract article content with AI.
可基于视觉特征快速使用 AI 提取文章的内容。

### Vision Data Structure / 视觉数据结构

Each element in the `vision` array contains:

`vision` 数组中每个元素包含以下字段：

| Field | Description |
|-------|-------------|
| `top`, `left`, `bottom`, `x`, `y` | Element position / 元素位置 |
| `width`, `height` | Element size / 元素尺寸 |
| `fontSize`, `fontWeight` | Font style / 字体样式 |
| `nodeName` | Tag name (e.g. DIV, P, H1) / 标签名 |
| `fullxpath` | Full XPath of the element / 完整 XPath |
| `scrollWidth`, `scrollHeight` | Scroll dimensions / 滚动尺寸 |

## Quick Start / 快速开始

A quick demo script `vision_tool.py` is provided for testing the `request.vision` API.

提供了快速调用示例脚本 `vision_tool.py`，可用于测试 `request.vision` 接口。

```bash
python src/vision_tool.py "https://example.com"
```

Results are saved to `vision_result.json` as a complete JSON array.
运行结果保存在 `vision_result.json` 中，为完整的 JSON 数组格式。

## AI Content Extraction / AI 内容提取

The output data can be read, understood, and processed by any mainstream AI model. You can build news content extraction features based on this data. The author has developed a probability-based algorithm to extract news titles, publication dates, and body text with a success rate of up to **97%**, outperforming Diffbot.

输出的结果可以被任何主流 AI 模型阅读、理解和提取。你可以基于此数据开发新闻内容提取功能，作者通过一种基于概率的算法提取新闻标题、发布时间与正文，成功概率高达 **97%**，高于 Diffbot。

## License / 开源协议

This project is licensed under the **MIT License** with an additional requirement:

本项目基于 **MIT 许可证** 发布，并附加以下要求：

> **Any project that uses or derives from the code in this repository must be open source.**
>
> **使用或衍生自本项目代码的项目必须开源。**

- Source code must be publicly available
- The same open source license must be inherited
- Modifications must be clearly documented
- 源代码必须公开
- 必须继承相同的开源协议
- 修改内容必须明确标注
