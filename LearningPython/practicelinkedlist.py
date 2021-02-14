class node:                         #creat the intial function to creat rhe linked list
    def __init__ (self, data = None):
        self.data = data
        self.next = None

     #Creating a rapper to wrap around the class
class linked_list:
    def __init__(self):
        self.head = node() # this collects the head or first value in the linked list and save it as head

    def append(self, data): # Function collects the value for the call at the bottom
        new_node = node(data) # creat a temperary new node and have the vales node function to this new node
        current  = self.head  # The varieable current wll ld the head of the list (first elemetn isn list)
        while current.next != None: # loop while the next of te current node is not equal to none
            current= current.next # mane the next value now become the current value
        current.next= new_node


    def length(self):  # Cllect the length of the linked list
        current =  self.head  # make the current value  be call current
        total = 0           # intial the total to be 0
        while current.next != None: #loop through the nxt element of the linked my_list
            total+= 1   #at one for each element whole next element is not empty
            current= current.next  # once it marked as one change to current element the to the next element beside the current element
            return total  # This is repeated until the current next ellement is 0, then return the total

    def display(self):
        element = []   # create the empty to list (not linked list)
        current_node = self.head # the node function that was saved in head is now save current node
        while current_node.next != None:  # loop throught the linked list that is now called current node and if the next value is not zero
            current_node=current_node.next # if the next value is not empty change the current node to the next node
            element.append(current_node.data) # put what was the current node in the empty list  that is element[]
        print element # once the function element is call it will print all the values that where added to the

    def get(self, index):  # collect index from the get function called at the bottom
        if index <= self.length(): # if the index value is greater than the function length
            print"error: 'Get' index out of range" # you will say it is out of range
            return None
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index : return current_node.data
            current_idx += 1

    def erase(self, index):
        if index >= self.length():
            print "error: 'errase ' index is out of range"
            return
            current_idx = 0
            current_node = self.head
            while True:
                last_node = current_node.next
                current_node = current_node.next
                if current_idx == index:
                    last_node.next = current_node.next
                    return
                current_idx +=1




my_list = linked_list()
my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()

my_list.erase(0)
my_list.display()

#print "element at 2nd index: %d" %my_list.get(4)
