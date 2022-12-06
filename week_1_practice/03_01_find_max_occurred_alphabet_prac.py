input = "hello my name is sparta"

def find_max_occurred_alphabet(string): # string 안에는 문자열이 들어갈 예정
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # a~z 까지의 26개의 배열 생성 (0 ~ 25)

    max_occurrence = 0                  # 문자열 안의 단어 최대 갯수 지정 초기값 0
    max_alphabet = alphabet_array[0]    # 초기값 알파벳을 배열 0번째인 'a'로 지정

    for alphabet in alphabet_array:     # 알파벳 배열 안에서 반복문 시작
        occurrence = 0                  # 문자열 안의 단어 갯수를 세기 위해 초기 값 0으로 지정
        for char in string:             # 주머진 문자 에서 반복문 시작. 주어진 문자열 : "hello my name is sparta"
            if char == alphabet:        # 주어진 문자열의 단어 중 알파벳 배열(a~z)에 있는 단어가 존재할 경우 True
                occurrence += 1         # 해당 단어의 갯수 카운트 +1

        if occurrence > max_occurrence:  # 해당 단어의 갯수가 문자열 안의 최대 갯수보다 많으면
            max_occurrence = occurrence # 해당 단어의 카운트한 수 만큼 최대 갯수로 바뀜
            max_alphabet = alphabet     # 해당 알파벳의 카운터 수 만큼 최대 갯수를 가지고 있는 알파벳으로 바꿈

        return max_alphabet             # 최대 갯수를 가지고 있는 알파벳을 반환


result = find_max_occurred_alphabet(input)
print(result)