class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            print(temp.data, "-->", end=" ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data, "-->", end=" ")
            print(temp.next.data)

    
    def add_begin(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new.next = self.head
            self.tail.next = new
            self.head = new
      
    def add_end(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            self.tail.next = new
            self.tail = new
            new.next = self.head
      
    def add_position(self,pos, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            if pos == 1:
                self.add_begin(x)
            else:
                temp = self.head
                for i in range(1, pos-1):
                    temp=temp.next
                new.next = temp.next
                temp.next = new
      

    def delete_begin(self):
        if self.head is None:
            print("Empty nothing to delete")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                self.head = temp.next
                temp = None
                self.tail.next = self.head
    
    def delete_end(self):
        if self.head is None:
            print("Empty nothing to delete")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                
                self.tail = None
                self.tail = temp
                self.tail.next = self.head
    
    def delete_position(self, pos):
        if self.head is None:
            print("Empty nothing to delete")
        elif pos == 1:
            self.delete_begin()
        else:
            temp1 = self.head
            temp2 = self.head.next
            for i in range(1, pos-1):
                temp1 = temp1.next
                temp2 = temp2.next
            
            temp1.next = temp2.next

            if temp2 == self.tail:
                self.tail = temp1
            temp2 = None
            


    def search(self, x):
        temp = self.head
        count = 0
        flag = 0
        while(temp != self.tail):
            if x == temp.data:
                flag = 1
                break
            temp = temp.next
            count = count + 1
        else:
            if x == temp.data:
                flag = 1
        if flag == 1:
            print(x, "in this position", count +1)
        else:
            print(x, "is not in this list")


l1=LinkedList()
l1.add_begin(10)
l1.search(10)

l1.display()



