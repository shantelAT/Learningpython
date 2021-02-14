class node:
    def __init__(self, data = None, next=None)
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self)
        self.head  = None

    def insert_at_beginng(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("This list is empty")
            return

        inter = self.head
        llstring = " "

        While inter :
            inter += str(inter.data) + "--->"
            inter = inter.next

        print(llstr)

if __name__ == "__main__"
