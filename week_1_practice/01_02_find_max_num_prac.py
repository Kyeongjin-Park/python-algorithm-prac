input = [3, 5, 6, 7, 2, 4]

def find_max_num(array):
    max_num = array[0]

    for num in array:
        if num > max_num:
            max_num = num
            print(max_num)

    return max_num

result = find_max_num(input)
print(result)