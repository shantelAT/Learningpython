class Stack():
    def __init__ (self):
        self.itemlist = []

    def push(self, item):
        self.itemlist.append(item)

    def pop(self):
        return self.itemlist.pop()

    def is_list_empty(self):
        return self.itemlist == []

def is_match(p, p2):
    if p == "{" and p2 == "}":
        return True
    elif p == "[" and p2 == "]" :
        return True
    elif p == "(" and p2 == ")" :
        return True
    else :
        return False

def is_parenthesis_balanced(paren_string):
    s = Stack()
    is_balance = True
    index = 0

    while index <len(paren_string) and is_balance:
        paren = paren_string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_list_empty():
                is_balance = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balance = False
        index =+ 1

    if s.is_list_empty() and is_balance:
        return True
    else:
        return False



print(is_parenthesis_balanced("{[({})]}"))
