import random

fin = open("input.txt", 'r')

a = [line.strip() for line in fin.readlines()]
k = int(a[0])
a.pop(0)

a.sort()

print(a)
rand = random.randint(0, len(a))
answer = a[rand]
a.pop(rand)

while len(a) != 0:
    for it, curr in enumerate(a):
        if answer.endswith(curr[:-1]):
            answer += curr[-1]
            a.pop(it)
            break
        elif answer.startswith(curr[1:]):
            answer = curr[0] + answer
            a.pop(it)
            break

print(answer)