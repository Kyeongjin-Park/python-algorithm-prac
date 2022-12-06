def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet

print(find_max_occurred_alphabet("hello my name is sparta"))


# 1. a~z 배열 저장
# 2. max_occurrence: 0 시작
# 3. max_alphabet: 'a' 시작
# 4. for alphabet은 alphabet_array(a~z)에서 반복 시작
# 5. 빈도수 0에서 시작
# 6. for alphabet안의 for char은 ("hello my name is sparta")의 문장에서 시작
# 7. char 이 알바벳 배열에 있는 단어와 같으면
# 8. occurrence 카운트 +1
# 9. occurrence가 max_occurrence보다 높으면 -> 아래 if 문 실행
# 10. for문 다시 시작 (4. ~ 9) 반복
# 11. 'z'까지 반복 후  max_alphabet 리턴