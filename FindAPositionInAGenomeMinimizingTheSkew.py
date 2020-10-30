import numpy as np

def MinimumSkewProblem(text):
    current = 0
    scews = []
    for char in text:
        if char == 'C':
            current -= 1
        if char == 'G':
            current += 1
        scews.append(current)
    return np.where(np.array(scews) == min(scews))[0]

text = input()
print(*[i + 1 for i in MinimumSkewProblem(text)])