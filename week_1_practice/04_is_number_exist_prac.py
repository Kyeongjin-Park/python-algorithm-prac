input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for element in array:           # array(배열)안의 요소를 element 라고 정의함
        if number == element:       # 만약 입력한 숫자가 배열 안에 있는 요소가 존재하면
            return True             # True 반환

    return False                    # 없으면 False 반환

result = is_number_exist(3, input)
print(result)