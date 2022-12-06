# 노드는 아래 두 가지 정보가 필요함
# 1. 칸에 있는 데이터
# 2. 다음 칸이 뭔지

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(5)
second_node = Node(12)
first_node.next = second_node