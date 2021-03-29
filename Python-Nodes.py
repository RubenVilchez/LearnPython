class Node:
    def __init__(self, value, node_link = None):
        self.value = value
        self.node_link = node_link

    def get_value(self):
        return self.value

    def set_node_link(self, node_link):
        self.node_link = node_link

    def get_node_link(self):
        return self.node_link


john = Node('node 1 value')
bob = Node('node 2 value')
billy = Node('node 3 value')

john.set_node_link(bob)
bob.set_node_link(billy)

node_variable = john.get_value()

print(node_variable)