def find_prime_under_number(number):
    prime_list=[]
    for i in range(2, number+1):
        for j in prime_list:
            if i % j == 0 and j * j <= i:
                break
        else:
            prime_list.append(i)

    return prime_list

print(find_prime_under_number(20))



# 한 번 소수의 특징을 다시 생각해볼게요.
#
# 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다. 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문입니다.
#
# 이를 이용해서 i * i ≤ n 일 때까지만 비교하시면 됩니다!