def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

print(find_max_occurred_alphabet("hello"))
print(ord('a'))



# 1. alphabet_occurrence_array에 0배열 26개 생성 [0, 0, 0, ... 0]
# 2. 문장을 변수 char에 저장하는데 문장 길이만큼 반복
# 3. 만약 문장안에서 단어가 "아닐" 경우 continue 연산을 수행하지 않고 넘어감
# 4. arr_index는 ord(char)을 사용하여 ASCII코드 값으로 변환해 'a'의 아스키 코드 값을 빼 a=0, b=1 c=2... 이런식으로 인덱스를 지정한.
# 5. 처음에 0 배열로 채워져 있던 alphabet_occurrence_array에 arr_index에 맞춰 인덱스가 들어오면 alphabet_occurrence_array에 +1을 추가함 // (2~5 반복)
# 6. max_occurrence 를 초기값 0 지정
# 7. max_occurrence_index를 초기값 0 지정
# 8. 변수 index를 alphabet_occurrence_array 배열의 길이만큼 반복. (26번)
# 9. alphabet_occurrence는 alphabet_occurrence_array[index]에 맞춰 안에 들어있는 값 호출 alphabet_occurrence_array[0] -> 0, alphabet_occurrence_array[4] -> 1 (2~5)반복하며 채워진 숫자 값 출력
# 10. 만약 alphabet_occuuurence 값이 max_occurrence 값보다 크면
# 11. alphabet_occurrence 값을 max_occurrence값으로 변경
# 12. 해당 index 값을 max_alphabet_index 값으로 변경 // (8~12 반복)
# max_alphabet_index 값 + ASCII코드 'a' 값인 97 더한 후 chr을 통해 ASCII코드 값을 문자로 변환 후 문자 반환
