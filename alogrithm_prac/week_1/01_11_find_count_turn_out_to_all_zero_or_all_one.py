input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) -1 ): # n-1로 하는 이유는 배열의 마지막은 비교할 필요 없음
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


# 012345 [인덱스]
# 011110 [값]

# 시작이 0이면 count_to_all_one +1
# 인덱스 0: 0, 인덱스 1: 1  다름 -> 인덱스 1이 1이므로 count_to_all_zero +1
# 인덱스 4: 1, 인덱스 5: 0  다름 -> 인덱스 5가 0이므로 count_to_all_one + 1

# 결론
# count_to_all_zero: 1
# count_to_all_one: 2
# min값 반환 -> 1
