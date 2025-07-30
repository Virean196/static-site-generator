from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links)

text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
html_node = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})

#print(html_node.props_to_html())

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

code_node = [TextNode("`This` is a code node", TextType.CODE)]

#print(node.to_html())

text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

