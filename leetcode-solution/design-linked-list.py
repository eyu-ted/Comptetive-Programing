class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def get(self, index: int) -> int:
        if self.head==None:
            return -1
        
        temp=self.head
        while index and temp:
            temp=temp.next
            index-=1
        if temp:
            return temp.value
        return -1
     

        

    def addAtHead(self, val: int) -> None:
        newnode=node(val)
        
        newnode.next=self.head
        self.head=newnode
        

    def addAtTail(self, val: int) -> None:
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.next=None
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        newnode=node(val)
        temp=self.head
    
        while index-1 and temp:
            prev=temp
            temp=temp.next
            index-=1
        if temp==None:
            temp=newnode
            temp.next=None
        tempindex=temp.next        
        temp.next=newnode
        newnode.next=tempindex

    def deleteAtIndex(self, index: int) -> None:

        if index==0:
            self.head=self.head.next
            return 
        temp=self.head        
        while index-1 and temp:
            temp=temp.next
            index-=1
        if temp and temp.next:
            indextemp=temp.next.next
            temp.next=indextemp
        return 
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)