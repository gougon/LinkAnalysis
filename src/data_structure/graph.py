from src.data_structure.node import Node


class Graph:
    def __init__(self):
        self.__nodes = []

    def __find(self, name):
        for node in self.__nodes:
            if node.name == name:
                return node
        new_node = Node(name)
        self.__nodes.append(new_node)
        return new_node

    def add_edge(self, parent, child):
        parent_node = self.__find(parent)
        child_node = self.__find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    def display(self):
        for node in self.__nodes:
            print('name: {}\n\tparents: {}\n\tchildren: {}'.format(node.name, node.parents, node.children))
