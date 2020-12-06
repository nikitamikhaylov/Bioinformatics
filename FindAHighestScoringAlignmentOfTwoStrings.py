import numpy as np

from decimal import Decimal

ALPHABET = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

SCORES_TABLE = """
4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
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

    score = dp[-1][-1]
    result1, result2 = [], []
    i, j = len(str2) - 1, len(str1) - 1
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


    print(int(score))
    print("".join(result1))
    print("".join(result2))


print(SCORES)

str1 = input()
str2 = input()

GlobalAlignmentProblem(str1, str2)