class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:                      # index가 0 번째일 경우
            self.head = self.head.next      # head노드의 다음을 head로 지정 (예외처리)
            return
        node = self.get_node(index - 1)     # 인덱스 앞의 노드 찾기
        node.next = node.next.next          # 현재 노드 next의 next를 노드의 next로 변경