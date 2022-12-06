class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node(5)            # 현재 next 가 없이 하나의 노드만 있음 [5]
second_node = Node(12)         # [12]를 들고 있는 노드 생성
first_node.next = second_node   # [5]의 next를 [12]로 지정 [5] -> [12]

print(first_node.data)          # 5
print(second_node.data)        # 12
print(first_node.next.data)     # 12