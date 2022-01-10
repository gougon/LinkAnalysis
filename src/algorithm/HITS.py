class HITS:
    def __init__(self, graph):
        self.__graph = graph

    def __update(self):
        for node in self.__graph.nodes:
            node.update_auth()
        for node in self.__graph.nodes:
            node.update_hub()
        self.__graph.normalize_auth_hub()

    def run(self, iteration):
        for i in range(iteration):
            self.__update()
        return self.__graph
