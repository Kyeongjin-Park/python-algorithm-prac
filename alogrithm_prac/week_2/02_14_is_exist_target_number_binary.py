finding_target = 2
finding_numbers = [0,3,5,6,1,2,4]

def is_exist_target_number_binary(target, array):
    for number in array:
        if target == number:
            return True

    else: False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)