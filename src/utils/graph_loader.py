from src.data_structure.graph import Graph
from configuration.constant import *


class GraphLoader:
    def __init__(self):
        self.__filepath = None
        self.__file_mode = None
        self.__graph = None

    def load_graph(self, filepath, file_mode):
        self.__filepath = filepath
        self.__file_mode = file_mode
        self.__transform()

    def __transform(self):
        with open(self.__filepath) as f:
            datas = f.readlines()

        self.__graph = Graph()
        for data in datas:
            if self.__file_mode == FileMode.GRAPH:
                [parent, child] = data.strip().split(',')
            else:
                [parent, child] = data.split()[1:]
            self.__graph.add_edge(parent, child)

    def get_graph(self):
        if self.__graph is None:
            raise Exception('Need to load graph.')
        return self.__graph
