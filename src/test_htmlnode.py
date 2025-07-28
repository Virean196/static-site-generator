import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_neq_tag(self):
        node = HTMLNode("h1", "This is heading text", None, None)
        node2 = HTMLNode("h2", "This is heading text", None, None)
        self.assertNotEqual(node, node2)

    def test_neq_value(self):
        node = HTMLNode("h1", "This is heading text", None, None)
        node2 = HTMLNode("h1", "This is also heading text", None, None)
        self.assertNotEqual(node, node2)
    
    def test_neq_children(self):
        node = HTMLNode("li", None, [HTMLNode("p","Item 1",None,None), HTMLNode("p","Item 2",None,None)],None)
        node2 = HTMLNode("li", None, [HTMLNode("p","Item 1",None,None)], None)
        self.assertNotEqual(node, node2)
    
    def test_neq_props(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", None, None, {"href": "https://www.bootdev.com"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank" ')