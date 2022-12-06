# [3] -> [4]
# Data, Next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        self.head.next = Node(data)


# [3] -> [4] -> [5] -> [6] -> None
linked_list = LinkedList(3)
print(linked_list.head.data)


print(node.next.data)

print(node.data)