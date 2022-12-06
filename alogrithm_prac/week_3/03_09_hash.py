class Dict:
    def __init__(self):                         # 배열의 길이로 나눈 나머지 값 사용
        self.items = [None] * 8                 # 예를 들어 배열의 길이가 8이라면, 8로 나눈 나머지는 0~7이기 때문에 무조건 배열 인덱스로 연결될 것이다

    def put(self, key, value):                  # put(key, value) : key에 해당하는 value 저장하기
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self,key):                          # get(key): key에 해당하는 value 가져오기
        index = hash(key) % len(self.items)
        return self.items[index]