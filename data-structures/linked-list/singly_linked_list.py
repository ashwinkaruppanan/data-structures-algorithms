class Node:
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_bigining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def insert_at_position(self,data,position):
        if self.head is None:
            self.head = Node(data)
            return
        
        if position == 1:
            self.head = Node(data, self.head)
            return
    
        prev = self.head
        itr  = self.head
        count = 0
        while itr:
            count += 1
            if count == position:
                itr = Node(data,itr)
                prev.next = itr
                return
            prev = itr
            itr = itr.next
        
    def remove_at_begining(self):
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next

    def remove_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        prev = None
        itr = self.head
        while itr.next:
            prev = itr
            itr = itr.next
        prev.next = None

    def remove_at_position(self,position):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if position == 1:
            self.remove_at_begining()
            return
        
        count = 0
        prev = self.head
        itr = self.head
        while itr:
            count += 1
            if count == position:
                prev.next = itr.next
                return
            prev = itr
            itr = itr.next

    def reverse_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
    def insert_values(self,arr):
        self.head = None
        for data in arr:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:       
            count += 1
            itr  = itr.next

        print(count)

    def print(self):
        itr = self.head

        if itr is None:
            print("Linked list is empty")
            return
        
        txt = ""
        while itr:
            txt += str(itr.data) + "-->"
            itr = itr.next
        print(txt)
            
sll = SinglyLinkedList()
# sll.insert_at_bigining(2)
# sll.insert_at_bigining(1)
# sll.insert_at_end(10)
# sll.insert_at_end(12)
sll.insert_values([1,2,3,4,6,7,8,9])
# sll.insert_at_position(5,9)
# sll.remove_at_begining()
# sll.remove_at_end()
# sll.remove_at_position(5)
sll.reverse_list()
sll.print()
# sll.get_length()