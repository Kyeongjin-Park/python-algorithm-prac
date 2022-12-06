class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value) # head 에 시작하는 Node 연결

    def append(self, value):    # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결
        cur = self.head
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다.
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()