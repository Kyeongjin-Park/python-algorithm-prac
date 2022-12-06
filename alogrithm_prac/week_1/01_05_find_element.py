def find_element (number, array):
    for element in array:
        if number == element:
            return True
    else:
        return False

print(find_element(7, [3,5,6,1,2,4]))


# 1. array안에 요소를 element로 변수 저장하여 반복
# 2. 만약 입력된 숫자와 element가 같으면 True 반환 -> True 종료
# 3. 배열이 끝까지 가서 반복이 끝나면 for-else를 통해 else실행 False 반환

# number: 6
# 3 -> 5 -> 6 -> True 반환 종료
# number: 2
# 3 -> 5 -> 6 -> 1 -> 2 -> True 반환 종료
# number: 5
# 3 -> 5 -> 6 -> 1 -> 2 -> 4 -> for-else에 의해 else가 실행되어 False 반환 종료