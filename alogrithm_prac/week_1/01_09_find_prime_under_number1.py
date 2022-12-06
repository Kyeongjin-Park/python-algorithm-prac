def find_prime_under_number (number):
    prime_list = []
    for i in range(2, number+1):
        for j in prime_list:
            if i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list

print(find_prime_under_number(20))


# prime_list 변수에 빈 배열 생성
# i 변수에 2 ~ 입력 숫자 +1 // 반복은 0부터 시작하기 때문에 20일 경우 19까지 나오므로 입력+1로 함
# j 변수에 prime_list요소 반복 -> 계속 false면 for-else에 의해 i의 요소를 prime_list로 저장 (반복)

# i:2 -> .append
# i:3 -> .append
# i:4 , j:2 -> break
# i:5 -> .append
# i:6, j:2 -> break
# i:7 -> .append
# i:8, j:2 -> break
# i:9, j:3 -> break
# ...


# 숫자가 19가 들어왔다고 해볼게요.
#
# 2, 3, 4, 5, 6, 7, 8, 9, ... 19까지 한 번씩 다 나누면서 나머지가 0인지 확인합니다.
#
# 그러나 2와 3으로 나누어 떨어지지 않는다면, 2 X 3 인 6으로도 당연히 안 나누어 떨어집니다. 즉, 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라, 2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선해봅시다.
#
# 그러면, 뭐가 소수인지는 어떻게 알 수 있을까요? 바로, 직전에 찾은 소수들을 이용하면 됩니다.