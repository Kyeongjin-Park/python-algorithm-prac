def find_alphabet_occurrence_array(string): 		# string <- hello my name is sparta
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue								# 알파벳이 아니면 코드를 수행하지 않고 넘어감
        arr_index = ord(char) - ord("a")			# ASCII 코드를 통해 문자 -> 숫자 변환하여 숫자 뻄
        alphabet_occurrence_array[arr_index] += 1	# 문장안에 알파벳이 있을 때마다 숫자 +1씩 카운트 됨

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))