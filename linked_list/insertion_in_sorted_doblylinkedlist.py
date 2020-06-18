#testing
#results = [('10', 'Mary'), ('9', 'John'), ('10', 'George'), ('9', 'Frank'), ('9', 'Adam')]
#results.sort(key=lambda x: (int(x[0]), x[1]), reverse=True)
#print(results)
class DoublyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def sortedInsert(head, data):
    traversal_node=head
    new_node=DoublyLinkedListNode(data)
    while traversal_node is not None:
        if traversal_node.data >= data:
            traversal_node.prev=new_node
            new_node.next=traversal_node
            new_node.prev=None
            head=new_node
            break
        if traversal_node.next is not None and data >=traversal_node.data and data <= traversal_node.next.data:
            print("here")
            new_node.next=traversal_node.next
            traversal_node.next=new_node
            new_node.prev=traversal_node
            traversal_node.next.prev=new_node
            break
        if data>=traversal_node.data and traversal_node.next is None:
            traversal_node.next=new_node
            new_node.next=None
            new_node.prev=traversal_node
            break
        traversal_node=traversal_node.next
    return head
def print_list(head):
    traversal_node=head
    while traversal_node is not None:
        print(traversal_node.data,end="<-->")
        traversal_node=traversal_node.next
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
new_head=sortedInsert(head,4)
print_list(new_head)
