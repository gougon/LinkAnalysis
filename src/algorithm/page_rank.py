class PageRank:
    def __init__(self, graph, d):
        self.__graph = graph
        self.__d = d

    def __update(self):
        n = len(self.__graph.nodes)
        for node in self.__graph.nodes:
            node.update_page_rank(self.__d, n)
        self.__graph.normalize_page_rank()

    def run(self, iteration):
        for i in range(iteration):
            self.__update()
        return self.__graph
