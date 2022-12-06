input = [4,6,2,9,1]

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i+j

        array[i], array[min_index] = array[min_index], array[i]
    return array

selection_sort(input)
print(input)

# a[0+0] = 4 < a[4] = 1
# a[0+1] = 6 < a[4] = 1
# a[0+2] = 2 < a[4] = 1
# a[0+3] = 9 < a[4] = 1
# a[0+4] = 1 < a[4] = 1    ->  [1,6,2,9,4]

# a[1+0] = 6 < a[4] = 4
# a[1+1] = 2 < a[4] = 4    ->  min_index = 2 -> a[1], [2] = a[2], a[1] -> [1,2,6,9,4]

# a[2+0] = 6 < a[4] = 4
# a[2+1] = 9 < a[4] = 4    ->  [1,2,4,9,6]

# a[3+0] = 9 < a[4] = 6    ->  [1,2,4,6,9]


# [4 6 2 9 1]
#  _       _
# [1 6 2 9 4]
#    _ _
# [1 2 6 9 4]
#      _ _
# [1 2 4 9 6]
#        _ _
# [1 2 4 6 9]
