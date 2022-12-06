def find_max_num (array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

print(find_max_num([3,5,6,1,2,4]))


# max_num 을 배열의 0번쨰인 3 저장
# max_num: 3 시작
# num: 3
# num: 5
# max_num: 5 저장
# num: 6
# max_num: 6 저장
# num: 1
# num: 2
# num: 4
# max_num: 6 반환



