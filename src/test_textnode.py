import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node with slightly different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://bootdev.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_empty_neq_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_url_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()