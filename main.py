from src.utils.graph_loader import GraphLoader
from src.algorithm.HITS import HITS
from src.algorithm.page_rank import PageRank
from src.algorithm.sim_rank import SimRank
from src.data_structure.similarity import Similarity
from configuration.config import *


def load_graph():
    graph_loader = GraphLoader()
    graph_loader.load_graph(DATA_FOLDER + DATA_FILE, FileMode.GRAPH)
    return graph_loader.get_graph()


graph = load_graph()
sim = Similarity(graph, DECAY_FACTOR)
print('Load complete')

if ALGORITHM == Algorithm.HITS:
    alg = HITS(graph)
elif ALGORITHM == Algorithm.PAGE_RANK:
    alg = PageRank(graph, DAMPING_FACTOR)
else:
    alg = SimRank(graph, sim)
result = alg.run(10)
result.display()
