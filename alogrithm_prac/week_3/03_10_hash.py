# 만약 해쉬의 값이 같으면 어떻게 될까요?
# 혹은 해쉬 값을 배열의 길이로 나눴더니 똑같은 숫자가 되면 어떡할까요?
#
# 같은 어레이의 인덱스로 매핑이 되어서 데이터를 덮어 써버리는 결과가 발생합니다.
#
# 이를 충돌(collision)이 발생했다고 합니다.
#
# 돌을 해결하는 첫번째 방법은 바로 링크드 리스트를 사용하는 방식입니다.
# 이 방식을 연결지어서 해결한다고 해서 체이닝(Chaining) 이라고 합니다!
#
# fast 의 해쉬 값과 slow 의 해쉬 값이 동일하게 3이 나왔다고 해볼게요.
#
# 현재 3번째 인덱스에 현재 fast 와 slow 가 서로 가지겠다고 싸우고 있습니다.
#
# 그러면, 둘을 아예 연결해주는거에요! 이렇게요!
#
# [None, None, (fast, "빠른") → (slow, "느린"), ... ]
#
# 아직 감이 안 오시죠?
# 이 데이터를 이용해서 개선된 딕셔너리를 만들면 느낌 오실거에요!


class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

#####################################################################

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

# 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린")] 이었다!
# 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
# self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게!

	def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

# 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린") -> ("fast", "빠른")] 이었다!
# 그렇다면 그 리스트를 돌면서 key 가 일치하는 튜플을 찾아준다.
# ("fast", "빠른") 이 일치하므로 "빠른" 이란 값을 돌려주자!


#  <Dictionary>
# list                             list
# [0] [LinkedTuple] ------------> [(key, value), (key, value), (key, value), (key, value)]
# [1] [LinkedTuple]
# [2] [LinkedTuple]
# [3] [LinkedTuple]
# [4] [LinkedTuple]
# [5] [LinkedTuple]
# [6] [LinkedTuple]
# [7] [LinkedTuple]


# 충돌을 해결하는 두 번째 방법은 배열의 다음 남는 공간에 넣는 것입니다!
#
# fast 의 해쉬 값이 3이 나와서 items[3] 에 들어갔습니다.
#
# 그런데 slow 의 해쉬 값이 동일하게 3이 나왔습니다.
#
# 그러면, items[4] 를 봅니다. 앗, 이미 차 있네요.
#
# 그러면 그 다음 칸인 items[5] 를 봅니다.
#
# 비어 있으니까 items[5] 에 slow 의 value 값을 넣는 방식을
#
# 개방 주소법(Open Addressing) 이라고 합니다!
# 이 방법은 따로 구현하지는 않겠습니다!


# 해쉬 테이블(Hash Table)은 "키" 와 "데이터"를 저장함으로써 즉각적으로 데이터를 받아오고 업데이트하고 싶을 때 사용하는 자료구조입니다.
#
# 해쉬 함수(Hash Function)는 임의의 길이를 갖는 메시지를 입력하여 고정된 길이의 해쉬값을 출력하는 함수입니다.
#
# 해쉬 테이블의 내부 구현은 키를 해쉬 함수를 통해 임의의 값으로 변경한 뒤 배열의 인덱스로 변환하여 해당하는 값에 데이터를 저장합니다.
#
# 그렇기 때문에 즉각적으로 데이터를 찾고, 추가할 수 있는 것 입니다.
#
# 만약, 해쉬 값 혹은 인덱스가 중복되어 충돌이 일어난다면?
#
# 체이닝과 개방 주소법 방법으로 해결할 수 있습니다!