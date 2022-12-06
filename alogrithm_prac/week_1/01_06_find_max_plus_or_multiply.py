def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for num in array:
        if num <= 1 or multiply_sum <= 1:
            multiply_sum += num
        else:
            multiply_sum *= num
    return multiply_sum

print(find_max_plus_or_multiply([3, 0, 5, 6, 1, 2, 4]))

# multiply_sum = 0 시작
# 0
# 0 + 3
# 0 + 3 + 0
# 0 + 3 + 0 * 5
# 0 + 3 + 0 * 5 * 6
# 0 + 3 + 0 * 5 * 6 + 1
# 0 + 3 + 0 * 5 * 6 + 1 * 2
# 0 + 3 + 0 * 5 * 6 + 1 * 2 * 4 = 728
