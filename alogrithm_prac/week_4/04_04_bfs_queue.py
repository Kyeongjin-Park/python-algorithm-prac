# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 3, 4],
#     2: [1, 5],
#     3: [1, 6, 7],
#     4: [1, 8],
#     5: [2, 9],
#     6: [3, 10],
#     7: [3],
#     8: [4],
#     9: [5],
#     10: [6]
# }
# visited = [] # 방문한 걸 저장하기 위한 배열
# queue = [1] # 시작 노드인 1을 넣어둔다.
#
# 1. 현재 큐에서 가장 처음에 넣은 1을 빼서, visited 에 추가합니다.
# # queue -> [] visited -> [1]
#
# 2. 인접한 노드들인 [2, 3, 4] 에서 방문하지 않은 것들인 [2, 3, 4]를 queue 에 추가합니다.
# # queue -> [2, 3, 4] visited -> [1]
#
# 3. 현재 큐에서 가장 처음에 넣은 2을 빼서, visited 에 추가합니다.
# # queue -> [3, 4] visited -> [1, 2]
#
# 4. 인접한 노드들인 [1, 5] 에서 방문하지 않은 것들인 [5]를 queue 에 추가합니다.
# # queue -> [3, 4, 5] visited -> [1, 2]
#
# 5. 현재 큐에서 가장 처음에 넣은 3을 빼서, visited 에 추가합니다.
# # queue -> [4, 5] visited -> [1, 2, 3]
#
# 6. 인접한 노드들인 [1, 6, 7] 에서 방문하지 않은 것들인 [6, 7]를 queue 에 추가합니다.
# # queue -> [4, 5, 6, 7] visited -> [1, 2, 3]
#
# 7. 현재 큐에서 가장 처음에 넣은 4을 빼서, visited 에 추가합니다.
# # queue -> [5, 6, 7] visited -> [1, 2, 3, 4]
#
# 8. 인접한 노드들인 [1, 8] 에서 방문하지 않은 것들인 [8]를 queue 에 추가합니다.
# # queue -> [5, 6, 7, 8] visited -> [1, 2, 3, 4]
#
# 9. 현재 큐에서 가장 처음에 넣은 5을 빼서, visited 에 추가합니다.
# # queue -> [6, 7, 8] visited -> [1, 2, 3, 4, 5]
#
# 10. 인접한 노드들인 [2, 9] 에서 방문하지 않은 것들인 [9]를 queue 에 추가합니다.
# # queue -> [6, 7, 8, 9] visited -> [1, 2, 3, 4, 5]
#
# 11. 현재 큐에서 가장 처음에 넣은 6을 빼서, visited 에 추가합니다.
# # queue -> [7, 8, 9] visited -> [1, 2, 3, 4, 5, 6]
#
# 12. 인접한 노드들인 [3, 10] 에서 방문하지 않은 것들인 [10]를 queue 에 추가합니다.
# # queue -> [7, 8, 9, 10] visited -> [1, 2, 3, 4, 5, 6]
#
# 13. 현재 큐에서 가장 처음에 넣은 7을 빼서, visited 에 추가합니다.
# # queue -> [8, 9, 10] visited -> [1, 2, 3, 4, 5, 6, 7]
#
# 14. 인접한 노드들인 [3] 에서 방문하지 않은 것들이 없으니 추가하지 않습니다.
# # queue -> [8, 9, 10] visited -> [1, 2, 3, 4, 5, 6, 7]
#
# 15. 현재 큐에서 가장 처음에 넣은 8을 빼서, visited 에 추가합니다.
# # queue -> [9, 10] visited -> [1, 2, 3, 4, 5, 6, 7, 8]
#
# 16. 인접한 노드들인 [4] 에서 방문하지 않은 것들이 없으니 추가하지 않습니다.
# # queue -> [9, 10] visited -> [1, 2, 3, 4, 5, 6, 7, 8]
#
# 17. 현재 큐에서 가장 처음에 넣은 9을 빼서, visited 에 추가합니다.
# # queue -> [10] visited -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 18. 인접한 노드들인 [5] 에서 방문하지 않은 것들이 없으니 추가하지 않습니다.
# # queue -> [10] visited -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 19. 현재 큐에서 가장 처음에 넣은 10을 빼서, visited 에 추가합니다.
# # queue -> [] visited -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 20. 인접한 노드들인 [6] 에서 방문하지 않은 것들이 없으니 추가하지 않습니다.
# # queue -> [] visited -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 21. 현재 큐에서 꺼낼 것이 없습니다. BFS 가 끝났습니다.
#
#
# 자... 어마어마한 내용들이 있었는데요!
# 이 코드를 보면 어떤 순서대로 BFS 가 이루어지는 지 조금은 이해가 가실 것 같습니다.
# 모든 순서를 외우실 필요는 없습니다 다만! 탐색의 순서와 느낌에 대해 이해가셨으면 좋겠습니다.



# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}



# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!