class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        props_string = ""
        for prop in self.props:
            props_string += f'{prop}="{self.props[prop]}" '
        return props_string
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.tag != None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"{self.value}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children = children, props = props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("children is missing")
        node_to_html = f"<{self.tag}>"
        for child in self.children:
            node_to_html += child.to_html()
        node_to_html += f"</{self.tag}>"
        return node_to_html