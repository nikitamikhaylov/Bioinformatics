import sys
sys.setrecursionlimit(1000000)

a = [[int(i) for i in chunk.strip('()').split()] for chunk in input().strip().split(')') if chunk]
b = [[int(i) for i in chunk.strip('()').split()] for chunk in input().strip().split(')') if chunk]

n = max([max([abs(x) for x in chunk]) for chunk in a])

visited = [False for _ in range(n * 2)]
graph = [[] for _ in range(n * 2)]

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

def id(value):
    if value < 0:
        return abs(value) * 2 - 1
    else:
        return value * 2 - 2

for chunk in a + b:
    chunk = chunk[::]
    chunk.append(chunk[0])
    for i in range(1, len(chunk)):
        v = id(chunk[i - 1])
        u = id(-1 * chunk[i])
        graph[v].append(u)
        graph[u].append(v)

answer = n

for v in range(len(visited)):
    if not visited[v]:
        dfs(v)
        answer -= 1

print(answer)