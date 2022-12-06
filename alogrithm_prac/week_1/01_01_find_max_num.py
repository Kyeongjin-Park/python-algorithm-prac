def find_max_num (array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num

print(find_max_num([3, 5, 6, 1, 2, 4]))




# num: 3
# compare_num: 3 -> 5 -> break

# num: 5
# compare_num: 3 -> 5 -> 6 -> break

# num: 6
# compare_num: 3 -> 5 -> 6 -> 1 -> 2 -> 4 -> for-else문 실행 -> return num 실행. 6반환


# for-else문 : 중간에 break 문으로 빠져나오지 않고 for 문이 모두 돌았을 경우 실행
