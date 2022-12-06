def solution(price):
    answer = 0
    if (price >= 500000):
        answer = price - (price * 20) // 100
    elif (price >= 300000):
        answer = price - (price * 10) // 100
    else:
        answer = price - (price * 5) // 100

    return answer

print(solution(150000))
print(solution(580000))