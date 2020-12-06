import numpy as np

from decimal import Decimal

ALPHABET = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

SCORES_TABLE = """
2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
-2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
-3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
-1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
-1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
-1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
-2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
-1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
-2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
-6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
-3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
"""

SCORES = [[int(x) for x in line.split(' ') if x] for line in SCORES_TABLE.split('\n') if line.strip()]
SIGMA = 5

def GlobalAlignmentProblem(str1, str2):
    dp = np.zeros((len(str2) + 1, len(str1) + 1))
    for i in range(len(str1)):
        dp[0][i + 1] = dp[0][i] - SIGMA

    for i in range(len(str2)):
        dp[i + 1][0] = dp[i][0] - SIGMA

    for i in range(len(str2)):
        for j in range(len(str1)):
            dp[i+1][j+1] = max(dp[i][j+1] - SIGMA, dp[i+1][j] - SIGMA,
                           dp[i][j] + SCORES[ALPHABET.index(str2[i])][ALPHABET.index(str1[j])])
            if dp[i+1][j+1] < 0:
                dp[i+1][j+1] = 0

    score, i, j = 0, 0, 0
    for x in range(len(str2) + 1):
        for y in range(len(str1) + 1):
            if score < dp[x][y]:
                score = dp[x][y]
                i = x - 1
                j = y - 1

    result1, result2 = [], []
    while i != -1 or j != -1:
        tmp = dp[i + 1][j + 1] - SCORES[ALPHABET.index(str2[i])][ALPHABET.index(str1[j])]
        if tmp != dp[i][j]:
            tmp = max(dp[i + 1][j], dp[i][j + 1])
            if tmp != dp[i + 1][j]:
                result1 = ["-"] + result1
                result2 = [str2[i]] + result2
                i -= 1
            else:
                result1 = [str1[j]] + result1
                result2 = ["-"] + result2
                j -= 1
        else:
            result1 = [str1[j]] + result1
            result2 = [str2[i]] + result2
            i -= 1
            j -= 1
        if tmp == 0:
            break


    print(int(score))
    print("".join(result1))
    print("".join(result2))


print(SCORES)

str1 = input()
str2 = input()

GlobalAlignmentProblem(str1, str2)