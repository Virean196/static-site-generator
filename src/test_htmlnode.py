import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    
    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grand_grandchildren(self):
        grand_grandchild_node = LeafNode("i", "grand_grandchild")
        grandchild_node = ParentNode("span", [grand_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><span><i>grand_grandchild</i></span></span></div>",)