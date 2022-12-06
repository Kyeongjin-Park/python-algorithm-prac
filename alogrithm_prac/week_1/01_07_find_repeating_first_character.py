def find_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    for char2 in string:
        if char2 in not_repeating_character_array:
            return char2

    return "-"


print(find_repeating_first_character("abbcaydcze"))

# 1. 26개의 0 배열 생 [0, 0, 0, 0, ... 0]
# 2. 문장을 변수 char에 저장하는데 문장 길이만큼 반복
# 3. 만약 문장안에서 단어가 "아닐" 경우 continue 연산을 수행하지 않고 넘어감
# 4. arr_index는 ord(char)을 사용하여 ASCII코드 값으로 변환해 'a'의 아스키 코드 값을 빼 a=0, b=1 c=2... 이런식으로 인덱스를 지정한.
# 5. 처음에 0 배열로 채워져 있던 alphabet_occurrence_array에 arr_index에 맞춰 인덱스가 들어오면 alphabet_occurrence_array에 +1을 추가함 // (2~5 반복)
# 6. not_repeating_character_array라는 빈 배열 생성
# 7. 1.에서 생성한 배열 길이만큼 index 요소 생성 (0 부터 시작)
# 8. alphabet_occurrence는 2. ~ 5.까지 반복하여 문장의 단어 갯수. 없으면 0 출력  a[0] ~ a[25]까지
# 9. 만약 alphabet_occurrence_array[인덱스] 값 중 1이 있으면
# 10. 빈 배열인 not_repeating_character_array에 .append를 통해 1이 있는 위치의 인덱스 값 + 'a'의 ASCII코드 값을 한다음 다시 문자로 변환하여 해당 단어 빈 배열에 저장 a[0]~[25]사이에서 카운트가 1인 것만 string 순서대로 저장 [y, d, z, e] 순서
# 11. char2는 주어진 문장에서 not_repeating_character_array를 반복 실행하여
# 12. True 값이 나오자마자 char2 반환하고 반복문 종료
# 13. 가장먼저 나오는 단어 y
