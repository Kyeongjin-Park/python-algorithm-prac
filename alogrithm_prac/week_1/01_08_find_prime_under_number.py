def find_prime_under_number (number):
    prime_list = []
    for i in range(2, number+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list

print(find_prime_under_number(20))


# prime_list라는 빈 배열 생성
# i는 1 ~ 숫자 + 1까지(시작, 끝) 저장 // 반복은 0부터 시작함. 20이면 0~19
# j는 2 ~ i(1~20) 저장
# 만약 i%j == 0 이면 break

# i = 2
# i:2 % j:2 -> 배열이 다 돌아서 for-else 실행 .append(i)에 2 추가
# i:3 % j:2, 3 -> 배열이 다 돌아서 for-else 실행 .append(i)에 3 추가
# i:4 % j:2 -> break
# i:5 % j:2, 3, 4, 5 -> 배열이 다 돌아서 for-else 실행 .append(i)에 5 추가
# ...
# i:15 % j:2, 3 -> break
# ...
# i:19 % j:2, 3, 4, 5, 6,  7, ... 19 -> 배열이 다 돌아서 for-else 실행 .append(i)에 19 추가
# i:20 % j:2 -> break



# 소수는 자기 자신과 1 외에는 아무것도 나눌 수 없습니다!
# 이 점을 이용해서 구현해보겠습니다.
#
# range 함수를 써서 2부터 number까지 반복문을 돕니다.
#
# 그리고 각 숫자를 n이라고 한다면, 2부터 n-1까지 n을 나눠봅니다.
# 그 때까지 안 나누어 떨어진다면? 소수입니다!