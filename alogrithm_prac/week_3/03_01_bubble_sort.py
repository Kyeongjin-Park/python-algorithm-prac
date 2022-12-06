input = [4,6,2,9,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):      # Q. 여기서ㅓ왜 n - i - 1 일까요?
            if array[j] > array[j + 1]:  # A. array[j] 와 array[j + 1] 을 비교할거라, 마지막 원소까지 가지 않아도 되기 때문이에요!
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

bubble_sort(input)
print(input)



# j => 5 - 0 - 1 : 4
# a[0]: 4 > a[1]: 6
# a[1]: 6 > a[2]: 2     -> [4, 2, 6, 9, 1]
# a[2]: 6 > a[3]: 9
# a[3]: 9 > a[4]: 1     -> [4, 2, 6, 1, 9]

# j => 5 - 1 - 1 : 3
# a[0]: 4 > a[1]: 2     -> [2, 4, 6, 1, 9]
# a[1]: 4 > a[2]: 6
# a[2]: 6 > a[3]: 1     -> [2, 4, 1, 6, 9]

# j => 5 - 2 - 1 : 2
# a[0]: 2 > a[1]: 4
# a[1]: 4 > a[2]: 1     -> [2, 1, 4, 6, 9]

# j => 5 - 3 - 1 : 1
# a[0]: 2 > a[1]: 1     -> [1, 2, 4, 6, 9]
