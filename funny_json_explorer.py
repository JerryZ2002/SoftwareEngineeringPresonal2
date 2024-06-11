# funny_json_explorer.py
from utils import load_json
from json_component import Leaf
from visitors import JsonVisitor
from json_iterator import JsonIterator

MAX_LENGTH = 40


class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory

    def _load(self, json_file):
        return load_json(json_file)

    def show(self, json_file):
        data = self._load(json_file)
        container = self.style_factory.create_container(self.icon_factory, "root", 0)
        self._parse_json(data, container)
        visitor = JsonVisitor(MAX_LENGTH)
        container.add_visitor(visitor)

    def _parse_json(self, data, container, level=1):
        iterator = JsonIterator(data)
        for key, value in iterator:
            if isinstance(value, dict):
                sub_container = self.style_factory.create_container(self.icon_factory, key, level)
                container.add(sub_container)
                self._parse_json(value, sub_container, level + 1)
            else:
                if value is not None:
                    key = f"{key}: {value}"
                leaf = Leaf(key, self.icon_factory.get_icon(is_leaf=True))
                container.add(leaf)
