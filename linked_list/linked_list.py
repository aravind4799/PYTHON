class node:
    def __init__(self,data):
        self.data=data
        self.next_node=None
    def has_value(self,value):
        if self.data==value:
            return True
        else:
            return False

class linked_list:
    def __init__(self):
        # note headnode should be a node object
        self.headnode=None

    def traverse(self):
        print_val=self.headnode
        while print_val is not None:
            print(print_val.data,end="-->")
            print_val=print_val.next_node

    def insert_at_begin(self,data_list):
        for data in data_list:
            new_node=node(data)
            if self.headnode is None:
                self.headnode=new_node
                continue
            new_node.next_node=self.headnode
            self.headnode=new_node

    def insert_at_end(self,data_list):
        for data in data_list:
            new_node=node(data)
            if self.headnode is None:
                self.headnode=new_node
                continue
            traversal_node=self.headnode
            while(traversal_node.next_node is not None):
                traversal_node=traversal_node.next_node
            traversal_node.next_node=new_node

    def insert_after(self,after_val,data):
        found=False
        traversal_node=self.headnode
        if traversal_node is None:
            print("LINKED LIST EMPTY")
        while(traversal_node is not None):
            if(traversal_node.data is after_val):
                found=True
                new_node=node(data)
                new_node.next_node=traversal_node.next_node
                traversal_node.next_node=new_node
            traversal_node=traversal_node.next_node
        if(found==False):
            print("no node is available with given data")

    def insert_before(self,data,value):
        prev=None
        if self.headnode==None:
            print("linked_list empty")
            return
        traversal_node=self.headnode
        # if this case , where in the node we search is headnode not handled,it makes
        #prev node None ,means prev.next throws error
        if traversal_node.has_value(data):
            new_node=node(value)
            new_node.next_node=traversal_node
            self.headnode=new_node
            return
        while traversal_node is not None and not traversal_node.has_value(data):
            prev=traversal_node
            traversal_node=traversal_node.next_node

        if traversal_node==None:
            print("data not found in linked_list")
            return
        new_node=node(value)
        prev.next_node=new_node
        new_node.next_node=traversal_node



    def insert_middle(self,data):
        # find the middle node
        count=0
        traversal_node=self.headnode
        if traversal_node is None:
            print("linked_list empty")
            return
        while(traversal_node is not None):
            count+=1
            traversal_node=traversal_node.next_node
        middle=count//2
        print(middle)
        middle_node=self.headnode
        for i in range(1,middle):
            middle_node=middle_node.next_node

        new_node=node(data)
        new_node.next_node=middle_node.next_node
        middle_node.next_node=new_node

    def remove(self,data):
        prev=None
        if self.headnode is None:
            print("linked_list is empty")
            return
        traversal_node=self.headnode
        while traversal_node is not None and not traversal_node.has_value(data):
            prev=traversal_node
            traversal_node=traversal_node.next_node
       #if we traversed entire list, means given data is not found
        if traversal_node is None:
            print("data not found")
            return
        # edge case where the node to remove is head_node
        if traversal_node is self.headnode:
            self.headnode=traversal_node.next_node
            return
        #if that case is not handled prev=None,so that prev.next throws error
        prev.next_node=traversal_node.next_node




    def swap_two_nodes(self,x_val,y_val):
        found_x=False
        found_y=False
        x_prev=None
        y_prev=None
        traversal_node_x=self.headnode
        traversal_node_y=self.headnode
        #checking whether linked_list  empty

        if self.headnode is None:
            print("linked list empty")
            return

        #finding x_val keeping track of node and its prev_node
        while traversal_node_x is not None:
            if traversal_node_x.has_value(x_val):
                found_x=True
                break
            x_prev=traversal_node_x
            traversal_node_x=traversal_node_x.next_node

        #finding y_val keeping track of node and its prev_node
        while traversal_node_y is not None:
            if traversal_node_y.has_value(y_val):
                found_y=True
                break
            y_prev=traversal_node_y
            traversal_node_y=traversal_node_y.next_node

        #if either of provided values is not found
        if not(found_x and found_y):
            print("given value is not found")
            return

        #check if traversal_node_x is head
        if x_prev!=None:
            x_prev.next_node=traversal_node_y
        else:
            self.headnode=traversal_node_y

        #check if traversal_node_y is head
        if y_prev!=None:
            y_prev.next_node=traversal_node_x
        else:
            self.headnode=traversal_node_x

        # swap the next_nodes of x and y
        print(traversal_node_x)
        temp=traversal_node_x.next_node
        traversal_node_x.next_node=traversal_node_y.next_node
        traversal_node_y.next_node=temp

    def reverse(self):
        curr_node=self.headnode
        prev=None
        next=None
        if curr_node is None:
            print("linked list is empty")
        while curr_node is not None:
            next=curr_node.next_node
            curr_node.next_node=prev
            prev=curr_node
            curr_node=next
        self.headnode=prev









lst0=[1,2,3,4]
lst1=[]
lst2=[]
linked_list=linked_list()

linked_list.insert_at_begin(lst0+lst1)
#linked_list.insert_at_end(lst0+lst1)
linked_list.traverse()
print("\n")
#linked_list.insert_middle(9_9)
#linked_list.remove_node(0)
linked_list.insert_before(4,5)
linked_list.traverse()
