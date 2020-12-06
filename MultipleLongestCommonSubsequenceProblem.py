import itertools
import numpy as np
a, b, c = input(), input(), input()

INF = 10 ** 9
dp = np.zeros((len(a) + 1, len(b) + 1, len(c) + 1))
dpf = [[[INF] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        for k in range(len(c) + 1):
            dir = [(x, y, z) for (x, y, z) in
                itertools.product(range(int(i != len(a)) + 1), range(int(j != len(b)) + 1), range(int(k != len(c)) + 1))]
            for (di, dj, dk) in dir:
                if di == 0 and dj == 0 and dk == 0:
                    continue
                value = dp[i][j][k] + int(di + dj + dk == 3 and a[i] == b[j] == c[k])
                if dp[i + di][j + dj][k + dk] < value or dpf[i + di][j + dj][k + dk] == INF:
                    dp[i + di][j + dj][k + dk] = value
                    dpf[i + di][j + dj][k + dk] = [di, dj, dk]

i, j, k = len(a), len(b), len(c)
ans = ['', '', '']
while i != 0 or j != 0 or k != 0:
    di, dj, dk = dpf[i][j][k]
    if di == 1:
        ans[0] += a[i - 1]
        i -= 1
    else:
        ans[0] += '-'
    
    if dj == 1:
        ans[1] += b[j - 1]
        j -= 1
    else:
        ans[1] += '-'

    if dk == 1:
        ans[2] += c[k - 1]
        k -= 1
    else:
        ans[2] += '-'

print(int(dp[len(a)][len(b)][len(c)]))
for a in ans:
    print(''.join(reversed(a)))
