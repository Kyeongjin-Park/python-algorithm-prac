input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            if compare_num > num:
                break
        else:
            return num
        print(num)



result = find_max_num(input)
print(result)