#**************  Learning Stacks

class Stack():
    def __init__ (self):
        self.itemlist = []

    def push(self, item):
        self.itemlist.append(item)

    def get_stack(self):
        return self.itemlist

    def pop(self):
        return self.itemlist.pop()

    def is_list_empty(self):
        return self.itemlist == []

s = Stack("A")
c = Stack("C")
s.push("d")
s.push("u")
s.push("m")
s.push("plin")

print(s.get_stack())
print(c.get_stack())
print(c.is_list_empty())
