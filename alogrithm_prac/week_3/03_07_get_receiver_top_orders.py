top_heights = [6,9,5,7,4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)                    # [0, 0, 0, 0, 0]
    while heights:
        height = heights.pop()                     # 맨 위의 값부터 하나하나 pop 하면서 원소들과 비교
        for idx in range(len(heights)-1, 0, -1):   # height의 길이-1, 0까지, -1씩
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer

print(get_receiver_top_orders(top_heights))


# heights = [6, 9, 5, 7, 4]
# answer = [0, 0, 0, 0, 0]
# heights.pop() -> 4 추출. => height = 4, heights = [6, 9, 5, 7]
# for idx = 4-1(=3) ~ 0까지 -1씩
# height[3]: 7 > height: 4
# answer[4] = 3 + 1 = 4


# answer = [0, 0, 0, 0, 4]
# heights.pop() -> 7 추출. => height = 7, heights = [6, 9, 5]
# for idx = 3-1(=2) ~ 0 까지 -1씩
# height[2]: 5 > height: 7
# height[1]: 9 > height: 7
# answer[3] = 1 + 1 = 2


# answer = [0, 0, 0, 2, 4]
# heights.pop() -> 5 추출. => height = 5, heights = [6, 9]
# for idx = 2-1(=1) ~ 0 까지 -1씩
# height[1]: 9 > height: 5
# answer[2] = 1 + 1 = 2


# answer = [0, 0, 2, 2, 4]
# heights.pop() -> 9 추출. => height = 9, heights = [6]
# for idx = 1-1(=0) ~ 0 까지 -1씩
# height[0]: 6 > height: 9
# answer[1] = 0 -> 아무 값도 일치하지 않아서 0 반환


# answer[0] = 0 -> 아무 값도 일치하지 않아서 0 반환