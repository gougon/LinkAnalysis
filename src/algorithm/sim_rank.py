from src.data_structure.graph import Graph
from src.data_structure.similarity import Similarity


class SimRank:
    def __init__(self, graph: Graph, sim: Similarity):
        self.__graph = graph
        self.__sim = sim

    def __update(self):
        for node1 in self.__graph.nodes:
            for node2 in self.__graph.nodes:
                self.__sim.update_sim_rank(node1, node2)
        self.__sim.update_sim()

    def run(self, iteration):
        for i in range(iteration):
            self.__update()
        return self.__graph
