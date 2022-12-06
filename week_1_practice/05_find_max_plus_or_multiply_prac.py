input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    multiply_sum = 0                                # 초기 합산 값
    for number in array:                            # 배열 안에 있는 요소를 number 안으로 정의함
        if number <= 1 or multiply_sum <= 1:        # number가 1보다 작거나 합산 값이 1보다 작으면
            multiply_sum += number                  # 넘버를 더하여 합산 값으로 넣는다
        else:                                       # number가 1보다 크거나 합산 값이 1보다 크면
            multiply_sum *= number                  # 넘버를 곱하여 합산 값으로 넣는다
    return multiply_sum                             # 합산 값을 반환한다.

result = find_max_plus_or_multiply(input)
print(result)