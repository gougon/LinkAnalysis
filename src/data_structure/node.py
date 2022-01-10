class Node:
    def __init__(self, name):
        self.name = name
        self.__children = []
        self.__parents = []
        self.auth = 1.0
        self.hub = 1.0
        self.page_rank = 1.0

    # properties
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def auth(self):
        return self.__auth

    @auth.setter
    def auth(self, val):
        self.__auth = val

    @property
    def hub(self):
        return self.__hub

    @hub.setter
    def hub(self, val):
        self.__hub = val

    @property
    def page_rank(self):
        return self.__page_rank

    @page_rank.setter
    def page_rank(self, val):
        self.__page_rank = val

    @property
    def parents(self):
        return self.__parents

    @property
    def children(self):
        return self.__children

    # functions
    def link_child(self, new_child):
        for child in self.__children:
            if child.name == new_child.name:
                return
        self.__children.append(new_child)

    def link_parent(self, new_parent):
        for parent in self.__parents:
            if parent.name == new_parent.name:
                return
        self.__parents.append(new_parent)

    # display
    def __repr__(self):
        return self.name
