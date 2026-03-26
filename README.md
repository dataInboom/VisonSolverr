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
