from src.utils.graph_loader import GraphLoader
from configuration.constant import *


graph_loader = GraphLoader()
for filename in GRAPH_FILES:
    graph_loader.load_graph(DATA_FOLDER + filename, FileMode.GRAPH)
    graph = graph_loader.get_graph()
    graph.display()
graph_loader.load_graph(DATA_FOLDER + IBM_FILE, FileMode.IBM)
graph = graph_loader.get_graph()
graph.display()
