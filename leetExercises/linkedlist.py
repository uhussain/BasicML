class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    #constructor
    def __init__(self):
        self.head=node()
    #add some functions
    def append(self,data):
        new_node=node(data)
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
        cur_node.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    def get(self,index):
        if index>=self.length():
            print("Error: out of range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=1

def main():
    mylist=linked_list()
    mylist.append(0)
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist.get(2))

if __name__ == '__main__':
    main()
