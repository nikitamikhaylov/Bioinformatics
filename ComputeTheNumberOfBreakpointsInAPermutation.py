a = input().strip('()')
a = [int(i) for i in a.split()]
a = [0] + a + [len(a) + 1]
ans = 0
for i in range(len(a) - 1):
    if a[i] + 1 != a[i + 1]:
        ans += 1

print(ans)