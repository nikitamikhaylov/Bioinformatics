def UniversalCircularStringProblem(k, n):
    alphabet = list(map(str, range(2)))

    a = [0] * k * n
    answer = []

    def helper(t, p):
        if t <= n:
            a[t] = a[t - p]
            helper(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                helper(t + 1, t)
        else:
            if n % p == 0:
                answer.extend(a[1 : p + 1])

    helper(1, 1)

    return "".join(alphabet[i] for i in answer)

k = int(input())
print(UniversalCircularStringProblem(2, k))