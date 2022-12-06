# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
# visited = [] # 방문한 걸 저장하기 위한 배열
# stack = [1] # 시작 노드인 1을 넣어둔다.
#
#
# 1. 현재 스택에서 가장 마지막에 넣은 1을 빼서, visited 에 추가합니다.
# # stack -> [] visited -> [1]
#
# 2. 인접한 노드들인 [2, 5, 9] 에서 방문하지 않은 것들인 [2, 5, 9]를 stack 에 추가합니다.
# # stack -> [2, 5, 9] visited -> [1]
#
# 3. 현재 스택에서 가장 마지막에 넣은 9을 빼서, visited 에 추가합니다.
# # stack -> [2, 5] visited -> [1, 9]
#
# 4. 인접한 노드들인 [1, 10] 에서 방문하지 않은 것들인 [10] 을 stack 에 추가합니다.
# # stack -> [2, 5, 10] visited -> [1, 9]
#
# 5. 현재 스택에서 가장 마지막에 넣은 10을 빼서, visited 에 추가합니다.
# # stack -> [2, 5] visited -> [1, 9, 10]
#
# 6. 인접한 노드들인 [9] 에서 방문하지 않은 노드들이 없으니 추가하지 않습니다.
# # stack -> [2, 5] visited -> [1, 9, 10]
#
# 7. 현재 스택에서 가장 마지막에 넣은 5를 빼서, visited 에 추가합니다.
# # stack -> [2] visited -> [1, 9, 10, 5]
#
# 8. 인접한 노드들인 [1, 6, 8] 에서 방문하지 않은 것들인 [6, 8]를 stack 에 추가합니다.
# # stack -> [2, 6, 8] visited -> [1, 9, 10, 5]
#
# 9. 현재 스택에서 가장 마지막에 넣은 8를 을 빼서, visited 에 추가합니다.
# # stack -> [2, 6] visited -> [1, 9, 10, 5, 8]
#
# 10. 인접한 노드들인 [5] 에서 방문하지 않은 노드들이 없으니 추가하지 않습니다.
# # stack -> [2, 6] visited -> [1, 9, 10, 5, 8]
#
# 11. 현재 스택에서 가장 마지막에 넣은 6을 빼서, visited 에 추가합니다.
# # stack -> [2] visited -> [1, 9, 10, 5, 8, 6]
#
# 12. 인접한 노드들인 [5, 7] 에서 방문하지 않은 것들인 [7] 을 stack 에 추가합니다.
# # stack -> [2, 7] visited -> [1, 9, 10, 5, 8, 6]
#
# 13. 현재 스택에서 가장 마지막에 넣은 7를 을 빼서, visited 에 추가합니다.
# # stack -> [2] visited -> [1, 9, 10, 5, 8, 6, 7]
#
# 14. 인접한 노드들인 [6] 에서 방문하지 않은 노드들이 없으니 추가하지 않습니다.
# # stack -> [2] visited -> [1, 9, 10, 5, 8, 6, 7]
#
# 15. 현재 스택에서 가장 마지막에 넣은 2를 빼서, visited 에 추가합니다.
# # stack -> [] visited -> [1, 9, 10, 5, 8, 6, 7, 2]
#
# 16. 인접한 노드들인 [1, 3] 에서 방문하지 않은 것들인 [3] 을 stack 에 추가합니다.
# # stack -> [3] visited -> [1, 9, 10, 5, 8, 6, 7, 2]
#
# 17. 현재 스택에서 가장 마지막에 넣은 3을 빼서, visited 에 추가합니다.
# # stack -> [] visited -> [1, 9, 10, 5, 8, 6, 7, 2, 3]
#
# 18. 인접한 노드들인 [2, 4] 에서 방문하지 않은 것들인 [4] 를 stack 에 추가합니다.
# # stack -> [4] visited -> [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]
#
# 19. 현재 스택에서 가장 마지막에 넣은 4를 빼서, visited 에 추가합니다.
# # stack -> [] visited -> [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]
#
# 20. 인접한 노드들인 [3] 에서 방문하지 않은 노드들이 없으니 추가하지 않습니다.
#
# 21. 현재 스택에서 꺼낼 것이 없습니다. DFS 가 끝났습니다.
#
#
#
# 여기서 조금 주의해야 할 점은, 아까 재귀로 구현한 방식과는 탐색하는 순서가 조금 다릅니다!
#
# 그러나, 가장 깊게 탐색하는 방식은 똑같습니다!
#
# 구현의 차이일뿐 개념은 동일하다는 점 이해하셨으면 좋겠습니다.
#
# 이 코드를 보면 어떤 순서대로 DFS 가 이루어지는 지 조금은 이해가 가실 것 같습니다.


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!