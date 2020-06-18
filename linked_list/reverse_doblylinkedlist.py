class DoublyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def print_list(head):
    traversal_node=head
    while traversal_node is not None:
        print(traversal_node.data,end="<-->")
        traversal_node=traversal_node.next

def reverse(head):
    temp=None
    traversal_node=head

    while traversal_node is not None:


        temp=traversal_node.prev
        traversal_node.prev=traversal_node.next
        traversal_node.next=temp
        traversal_node=traversal_node.prev
    print("\n"+str(count))
    if temp is not None:
        head=temp.prev
    return head
node1=DoublyLinkedListNode(1)
node2=DoublyLinkedListNode(3)
node3=DoublyLinkedListNode(4)
head=node1
node1.next=node2
node2.next=node3
node2.prev=node1
node3.prev=node2
print_list(head)
print("\n")
new_head=reverse(head)
print_list(new_head)
