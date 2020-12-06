a = input().strip('()')
a = [int(i) for i in a.split()]

for i in range(len(a)):
    j = a.index(i + 1) if i + 1 in a else a.index(-i - 1)
    if i != j:
        a = a[:i] + list(map(lambda x : -x, reversed(a[i:j+1]))) + a[j+1:]
        print('(' + ' '.join(map(lambda x: '{:+d}'.format(x), a)) + ')')
    if a[i] < 0:
        a[i] = abs(a[i])
        print('(' + ' '.join(map(lambda x: '{:+d}'.format(x), a)) + ')')
