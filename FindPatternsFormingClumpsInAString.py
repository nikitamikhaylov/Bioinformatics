import collections
from tqdm import tqdm

def ClumpsFindingProblem(k, L, t, text):
    answer = set()
    for sub_str in tqdm([text[i: i + L] for i in range(len(text) - L + 1)]):
        patterns = collections.defaultdict(int)
        for sub_pattern in [sub_str[i: i + k] for i in range(len(sub_str) - k + 1)]:
            patterns[sub_pattern] += 1
        for key, value in patterns.items():
            if value >= t:
                answer.add(key)
    return answer

text = input()
k, L, t = map(int, input().split())
print(*ClumpsFindingProblem(k, L, t, text))
