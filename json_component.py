# json_component.py
from abc import ABC, abstractmethod, ABCMeta


class JsonComponent(ABC):
    @abstractmethod
    def draw(self, prefix='', max_length=0):
        pass

    @abstractmethod
    def add_visitor(self, visitor):
        pass



class Leaf(JsonComponent):
    def __init__(self, name, icon=None):
        self.name = name
        self.icon = icon

    def draw(self, prefix='', max_length=0):
        line = f"{prefix}  {self.icon} {self.name} "
        line += '─' * (max_length - len(line) - 1) + "┤"
        print(line)

    def add_visitor(self, visitor):
        visitor.visit(self)


class JsonContainer(JsonComponent, metaclass=ABCMeta):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def __iter__(self):
        return iter(self.children)

    @abstractmethod
    def draw(self, prefix='', max_length=0):
        pass

    def add_visitor(self, visitor):
        visitor.visit(self)
        for child in self:
            child.add_visitor(visitor)
