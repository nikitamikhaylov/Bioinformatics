
def TheChangeProblem(coins, value):
    result = []
    for i in coins:
        if value % i == 0:
            result.append(value // i)
    greedy = {}
    while value != 0:
        greedy[max(coins)] = value // max(coins)
        value = value % max(coins)
        coins.remove(max(coins))
    result.append(sum(greedy.values()))
    return min(result)

n = int(input())
a = [int(i) for i in input().split(',')]

print(TheChangeProblem(a, n))