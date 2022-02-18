class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_parent(self):
        return self.parent

    def get_children(self):
        c = self.children
        return c

    def print_tree(self):
        prefix = ''
        if self.get_level() > 0:
            prefix = ' ' * self.get_level() * 6 + '|__'
        print(prefix, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root_node = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    root_node.add_child(laptop)

    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("IBM"))
    laptop.add_child(TreeNode("HP"))

    tv = TreeNode("TV")
    root_node.add_child(tv)

    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))

    phone = TreeNode("Cellphone")
    root_node.add_child(phone)

    phone.add_child(TreeNode("Apple"))
    phone.add_child(TreeNode("Google"))

    return root_node


if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    pass