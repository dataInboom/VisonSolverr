#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import requests
from lxml import html


class FlaresolverUtil:
    @staticmethod
    def VisionHtml(url):
        """
        调用 FlareSolverr 获取页面的视觉信息
        """
        try:
            response = requests.post(
                'http://127.0.0.1:8191/v1',
                json={
                    'cmd': 'request.vision',
                    'url': url,
                    'maxTimeout': 60000
                },
                timeout=70
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求 FlareSolverr 失败: {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"解析 JSON 响应失败: {e}", file=sys.stderr)
            return None


def vision_tool(url):
    """
    视觉工具主函数
    """
    vision = FlaresolverUtil.VisionHtml(url)

    if vision is not None:
        status = vision.get("status")

        if status == 200:
            response = vision.get("response")
            url = vision.get("url")

            # 使用 lxml 解析 HTML
            doc = html.fromstring(response)
            info = vision.get("vision")

            if info:
                for key in info.keys():
                    node = info[key]
                    node_name = node.get("nodeName")

                    # 获取完整 XPath 并转为小写
                    fullxpath = node.get("fullxpath").lower()

                    # 使用 XPath 查找元素
                    elements = doc.xpath(fullxpath)

                    if len(elements) > 0:
                        # 获取子节点数量
                        nodesize = len(elements[0])

                        if nodesize == 1 or nodesize == 0:
                            # 获取文本内容
                            text = elements[0].text_content()
                            text = str(text) if text is not None else ""

                            # 判断文本长度和节点类型
                            if len(text) > 6 and node_name != "A":
                                node["text"] = text
                                print(json.dumps(node, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vision_tool.py <url>")
        print("Example: python vision_tool.py http://finance.people.com.cn/n1/2026/0306/c1004-40676058.html")
        sys.exit(1)

    url = sys.argv[1]
    vision_tool(url)
