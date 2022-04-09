class Node:
    data = None
    next = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

class SinglyLinkedList:
    start = None

    def insert(self, data):
        if self.start == None:
            temp_node = Node(data, None)
            self.start = temp_node
            return

        temp_node = Node(data, self.start)
        self.start = temp_node
        return

    def print_linked_list(self):
        temp = self.start
        while temp != None:
            print(temp.data)
            temp = temp.next


list1 = [40,30,20,10]
sll = SinglyLinkedList()

for data in list1:
    sll.insert(data)

sll.print_linked_list()



