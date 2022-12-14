class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, value):       # 현재 [4] -> [2] 인 상태에서
        new_node = Node(value)      # [3] 을 만들고
        if self.is_empty():                 # 만약 비어 있다면,
            self.head = new_node            # head 에 new_node를
            self.tail = new_node            # tail 에 new_node를 넣어준다
            return

        self.tail.next = new_node   # 현재 tail 인 [2] 의 다음을 [3] 으로 저장
        self.tail = new_node        # 그리고 tail을 [3] 으로 지정


    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"    # 만약 비어있다면 에러!

        delete_head = self.head         # 제거할 node를 변수에 잡는다.
        self.head = self.head.next      # 그리고 head를 현재 head 의 다음 걸로 잡으면 된다.

        return delete_head.data         # 그리고 제거할 node 반환


    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data


    def is_empty(self):
        return self.list.head is None