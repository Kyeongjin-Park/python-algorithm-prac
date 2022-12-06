input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26            # 0~25 까지의 0 배열 생성

    for char in string:                             # 입력 문자열을 char요소로 정의하여 반복
        if not char.isalpha():                      # 만약 char의 요소 중 문자가 아니라면
            continue                                # 함수를 실행하지 않고 그냥 넘어간다
        arr_index = ord(char) - ord('a')            # char을 ASCII코드로 변환후 'a'의 값을 빼서 arr_index로 정의
        alphabet_occurrence_array[arr_index] += 1   # (1) 결과

    not_repeating_character_array = []                          # 배열 생성
    for index in range(len(alphabet_occurrence_array)):         # alphabet_occurrence_array 길이만큼 인덱스 생성 0~25
        alphabet_occurrence = alphabet_occurrence_array[index]  # 인덱스에 맞춰 input의 단어 갯수 넣음 ex) a=4, b=2, ... z=0

        if alphabet_occurrence == 1:                                        # input의 단어 갯수 중 1개가 있는 경우
            not_repeating_character_array.append(chr(index + ord("a")))     # index + a의 ASCII코드 수 더하여 배열 요소 추가 // (2) 결과

    for char in string:                             # 입력 문자열을 char요소로 정의하여 반복
        if char in not_repeating_character_array:   # 반복되지 않는 첫번째 문자가 발견될 경우
            return char                             # char로 반환한다

    return "_"      # 반복 안하는게 없는 경우 '_' 반환

result = find_not_repeating_first_character(input)
print(result)
