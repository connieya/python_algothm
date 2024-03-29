import sys
sys.stdin = open('input.txt')
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트를 만들고,모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
     # A에서 B로 가는 비용은 C라고 설정
    graph[a][b] = c

# 플로이드 워설 알고리즘 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j] , graph[i][k]+graph[k][j])


# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")

    print()


