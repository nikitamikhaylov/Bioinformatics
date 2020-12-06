import numpy as np
import sys

def LongestPath(n, m, down, right):
    result = [[0] * (m + 1) for _ in range(n+1)]
    for i in range(1, n + 1):
        result[i][0] = result[i-1][0] + down[i-1][0]
    for j in range(1, m + 1):
        result[0][j] = result[0][j-1] + right[0][j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result[i][j] = max(right[i][j-1] + result[i][j-1], down[i-1][j] + result[i-1][j])
    return result[n][m]


n, m = [int(i) for i in input().split()]

down = [[int(i) for i in input().split()] for _ in range(n)]
input()
right = [[int(i) for i in input().split()] for _ in range(n+1)]

print(down)
print(right)

print(LongestPath(n,m,down,right))