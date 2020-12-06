from collections import defaultdict
fin = open("input.txt", 'r')

a = [line.strip() for line in fin.readlines()]
k, d = map(int, a[0].split())
a.pop(0)

graph = defaultdict(list)
count = defaultdict(int)

for left, right in [pair.split('|') for pair in a]:
    prefix = (left[:-1], right[:-1])
    suffix = (left[1:], right[1:])
    graph[prefix].append(suffix)
    count[prefix] += 1
    count[suffix] -= 1

start = None
for key, value in count.items():
    if value > 0:
        start = key
        break

stack = [start]
path = []
while len(stack) > 0:
    curr = stack[-1]
    if graph.get(curr):
        if len(graph[curr]) != 0:
            next = graph[curr][0]
            stack.append(next)
            graph[curr].remove(next)
    else:
        path.append(stack.pop())

path = path[::-1]

answer = path[0][0]
answer += "".join(left[-1] for left, _ in path[1: d + 2])
answer += path[0][1]
answer += "".join(right[-1] for _, right in path[1:])

print(answer)

