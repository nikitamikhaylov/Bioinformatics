import itertools
from FindAllApproximateOccurrencesOfAPatternInAString import ApproximatePatternMatching

def FrequentWordsWithMismatchesProblem(text, k, d):
    patterns = {''.join(pattern): 0 for pattern in itertools.product("ACTG", repeat=k)}
    for pattern in patterns.keys():
        patterns[pattern] = ApproximatePatternMatching(text, pattern, d)
    frequency = max(patterns.values())
    answer = []
    for key, value in patterns.items():
        if value == frequency:
            answer.append(key)
    return answer


if __name__ == "__main__":
    text = input()
    k, d = map(int, input().split())
    print(*FrequentWordsWithMismatchesProblem(text, k, d))