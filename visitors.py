# visitors.py


class JsonVisitor:
    def __init__(self, max_length):
        self.max_length = max_length

    def visit(self, component):
        component.draw(max_length=self.max_length)

