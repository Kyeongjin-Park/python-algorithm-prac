class Node:                             # 노드 생성
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:                       # 링크드 클래스 생성
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):            # 새로운 노드 붙이기
        cur = self.head
        while cur is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self, value):         # LinkedList 가장 끝에 있는 노드에 새로운 노드 연결
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):          # LinkedList 원소 찾기
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):   # 링크드리스트 노트 추가
        new_node = Node(value)
        if index == 0:                  # 만약 0이 입력되면 get_node(-1)이 호출 될 수 있기에 예외처리함
            new_node.next = self.head   # 새로운 노드의 next를 현재 가지고 있는 head에 연결하고
            self.node = new_node        # 우선 현재 가지고 있는 head노드를 새로운 노드로 교체
            return

        node = self.get_node(index - 1) # 붙일 노드의 이전 노드
        next_node = node.next           # [node] -> [next_node] -> None
        node.next = new_node            # [node] -> [next_node] |=> [new_node]
        new_node.next = next_node       # [node] -> [new_node] -> [next_node]