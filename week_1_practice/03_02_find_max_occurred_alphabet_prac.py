input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26    # 0 배열 26개 생성

    for char in string:           # 입력 문자열 안에서 반복 시작. char 변수에 저장
        if not char.isalpha():    # char 변수 안에 '.isalpha()'를 사용하여 문자인지 판별. 만약 문자가 아닐 경우
            continue              # 아래 내용을 수행하지 않고 그냥 넘어감
        arr_index = ord(char) - ord("a")    # 'ord()를 사용해 문자를 ASCII코드로 변경 후 arr_index에 저장
        alphabet_occurrence_array[arr_index] += 1   # 공백을 제외한 단어 개수 만큼 h부터 시작해서 카운트 후 마지막 a까지 배열 반복 (총 19번)

    max_occurrence = 0          # 초기 알파벳 최고 갯수
    max_alphabet_index = 0      # 초기 알파벳 최고 갯수의 인덱스

    for index in range(len(alphabet_occurrence_array)):     # 0 배열의 길이만큼 숫자 반복(0 ~ 25) 총 26개
        alphabet_occurrence = alphabet_occurrence_array[index]      # 바로 위에서 만든 index의 위치에 맞게 카운트 된 단어의 갯수가 들어감

        if alphabet_occurrence > max_occurrence:    # 만약 카운트 된 알파벳 갯수가 기존 알파벳 최고 갯수보다 많다면
            max_occurrence = alphabet_occurrence    # 더 많이 카운트 된 알파벳 갯수로 바꿈
            max_alphabet_index = index              # 더 많이 카운트 된 알파벳 갯수의 인덱스로 바꿈
        return chr(max_alphabet_index + ord("a"))  # chr()을 통해 ASCII 코드 값을 "실제 문자"로 변경


result = find_max_occurred_alphabet(input)
print(result)

