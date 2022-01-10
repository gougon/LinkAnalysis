import copy


class Similarity:
    def __init__(self, graph, decay_factor):
        self.__decay_factor = decay_factor
        self.__name_list, self.__sim = self.__init_sim(graph)
        node_len = len(self.__name_list)
        self.__new_sim = [[0] * node_len for _ in range(node_len)]

    def __init_sim(self, graph):
        nodes = graph.nodes
        name_list = [node.name for node in nodes]
        sim = []
        for name1 in name_list:
            sim_row = []
            for name2 in name_list:
                if name1 == name2:
                    sim_row.append(1)
                else:
                    sim_row.append(0)
            sim.append(sim_row)
        return name_list, sim

    def __get_sim_val(self, node1, node2):
        node1_idx = self.__sim.index(node1.name)
        node2_idx = self.__sim.index(node2.name)
        return self.__sim[node1_idx][node2_idx]

    def update_sim_rank(self, node1, node2):
        if node1.name == node2.name:
            return 1.0

        in_links1 = node1.parents
        in_links2 = node2.parents

        total_sim_rank = 0
        for in_link1 in in_links1:
            for in_link2 in in_links2:
                total_sim_rank += self.__get_sim_val(in_link1, in_link2)

        sim_rank = self.__decay_factor / (len(in_links1) * len(in_links2)) * total_sim_rank

        node1_idx = self.__name_list.index(node1.name)
        node2_idx = self.__name_list.index(node2.name)
        self.__new_sim[node1_idx][node2_idx] = sim_rank

    def update_sim(self):
        self.__sim = copy.deepcopy(self.__new_sim)
