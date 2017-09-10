class Node:
    def __init__ (self, id, value, parent):
        self.id = id
        self.parent = parent
        self.child1= None
        self.child2 = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, id, value):
        if self.root is None:
            self.root = Node(id, value, None)
        else:
            return insert(self.root,id, value)

    def find(self, id):
        return find(self.root, id)

    def traverse(self, mickey_mouse):
        traverse (self.root, mickey_mouse)


def insert (node, id, value):
    if id > node.id:
        if node.child2 is None:
            node.child2 = Node(id, value, node)
        else:
            return insert(node.child2, id, value)

    elif id < node.id:
        if node.child1 is None:
            node.child1 = Node(id,value, node)
        else:
            return insert(node.child1, id, value)
    else:
        old_value = node.value
        node.value = value
        return old_value



def traverse (node, mickey_mouse):
    if node is not None:
        traverse(node.child1, mickey_mouse)
        mickey_mouse(node.id, node.value)
        traverse(node.child2, mickey_mouse)


def find(node, id):
    if node is None:
        return None
    if node.id == id:
        return node.value
    if node.id < id:
        return find(node.child2, id)
    if node.id > id:
        return find(node.child1, id)


def main():
    my_tree = Tree()
    my_tree.insert(13,"moo")
    my_tree.insert(5,"oink")
    my_tree.insert(2,"bawk")
    my_tree.insert(7,"neigh")
    my_tree.insert(21,"woof")
    my_tree.insert(1,"meow")
    my_tree.insert(4,"baah")
    my_tree.insert(15,"heehaw")
    my_tree.insert(17,"roar")
    my_tree.insert(12,"squeak")
    my_tree.insert(3,"chirp")
    my_tree.insert(14,"cheap")
    my_tree.insert(19,"cacaw")
    my_tree.insert(31,"awhoo")
    my_tree.insert(22,"meep")
    my_tree.insert(-5,"lol")
    print(my_tree.insert(-5,"lo"))
    my_tree.insert(-12,"me")
    my_tree.insert(42,"je")
    my_tree.insert(-17,"no")
    my_tree.insert(23,"not")
    my_tree.traverse(print)

    print(my_tree.find(21))



main()

