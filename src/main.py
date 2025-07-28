from textnode import TextNode, TextType
from htmlnode import HTMLNode

text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
html_node = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})

print(html_node.props_to_html())