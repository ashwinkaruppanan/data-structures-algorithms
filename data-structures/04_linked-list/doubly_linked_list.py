class Node:
    def __init__(self, prev = None,data = None,next = None) -> None:
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        node = Node(data=data,next=self.head)
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        
        self.head = node


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data=data)
            self.tail = self.head
            return
        
        self.tail.next = Node(prev=self.tail,data=data)
        self.tail = self.tail.next

    def insert_at_position(self,data, position):
        count = 0
        itr = self.head
        prev = self.head
        if position == 1:
            self.insert_at_beginning(data=data)
            return
        while itr:
            count += 1
            if count == position:
                prev.next = Node(prev=prev,data=data,next=itr)           
                itr.prev = prev.next     
                return
            prev = itr
            itr = itr.next
    
    def remove_at_beginning(self):
        if self.head is None:
            print("list is empy")
            return

        self.head = self.head.next
        self.head.prev = None

    def remove_at_end(self):
        if self.head is None:
            print("list is empty")
            return
        
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at_position(self,position):
        if self.head is None:
            print("list is empty")
            return
        
        if position == 1:
            self.remove_at_beginning()
            return

        count = 0
        itr = self.head
        prev = None
        next = None

        while itr:
            count += 1
            next = itr.next
            prev = itr.prev
            if count == position:
                if itr != self.tail:
                    itr.next.prev = prev
                    itr.prev.next = next
                    return
                else:
                    prev.next = None
                    self.tail = prev
                    return
            itr = itr.next

    def swap(self,value1,value2):
        ptr1 = self.head
        prev1 = None
        next1 = None
        ptr2 = self.head
        prev2 = None
        next2 = None
        itr = self.head
        while itr:
            if itr.data == value1:
                ptr1 = itr
                prev1 = itr.prev
                next1 = itr.next
            if itr.data == value2:
                ptr2 = itr
                prev2 = itr.prev
                next2 = itr.next
            itr = itr.next
        
        if prev1 != None:
            prev1.next = ptr2
        else:
            self.tail = ptr1
        ptr2.prev = prev1
        ptr2.next = next1
        next1.prev = ptr2
        prev2.next = ptr1
        ptr1.prev = prev2
        ptr1.next = next2
        if next2 != None:
            next2.prev = ptr1 
        else:
            self.head = ptr2

    def insert_values(self,arr):
        for i in arr:
            self.insert_at_end(i)

    def reverse_traversal(self):
        out = ""
        itr = self.tail
        while itr:
            out += str(itr.data) + "-->"
            itr = itr.prev
        print(out)

    def print(self):
        out = ""
        itr = self.head

        while itr:
            out += str(itr.data) + "-->"
            itr = itr.next
        print(out)

dll = DoublyLinkedList()
dll.insert_values([1,2,3,4,5,6,7,8,9])
# dll.insert_at_beginning(0)
# dll.insert_at_position(0,4)
# dll.remove_at_beginning()
# dll.remove_at_end()
# dll.remove_at_position(3)
dll.swap(3,7)
dll.print()
dll.reverse_traversal()
