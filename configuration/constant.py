from enum import Enum


class FileMode(Enum):
    GRAPH = 1
    IBM = 2


class Algorithm(Enum):
    HITS = 1
    PAGE_RANK = 2
    SIM_RANK = 3


DATA_FOLDER = 'datas/'
