input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):   # 1, 2, 3, 4
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break
    return array

insertion_sort(input)
print(input)


# array[1-0-1]: 4  > array[1-0]: 6

# array[2-0-1]: 6 > array[2-0]: 2 -> [4,2,6,9,1]
# array[2-1-1]: 4 > array[2-1]: 2 -> [2,4,6,9,1]

# array[3-0-1]:6 > array[3-0]: 9
# array[3-1-1]:4 > array[3-1]: 6
# array[3-2-1]:2 > array[3-2]: 4

# array[4-0-1]: 9 > array[4-0]: 1 -> [2,4,6,1,9]
# array[4-1-1]: 6 > array[4-1]: 1 -> [2,4,1,6,9]
# array[4-2-1]: 4 > array[4-2]: 1 -> [2,1,4,6,9]
# array[4-3-1]: 2 > array[4-3]: 1 -> [1,2,4,6,9]


# [4 6 2 9 1]
#    _ _
# [4 2 6 9 1]
#  _ _
# [2 4 6 9 1]

#        _ _
# [2 4 6 1 9]
#      _ _
# [2 4 1 6 9]
#    _ _
# [2 1 4 6 9]
#  _ _
# [1 2 4 6 9]