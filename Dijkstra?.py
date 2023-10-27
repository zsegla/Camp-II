# https://codeforces.com/problemset/problem/20/C



from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))
    graph[y].append((x, c))

dist = [1 << 60] * (n + 1)
prev = [-1] * (n + 1)
dist[1] = 0

queue = [(0, 1)]

while queue:
    distance, node = heappop(queue)

    if dist[node] != distance:
        continue

    for neighbor, cost in graph[node]:
        if dist[neighbor] > distance + cost:
            dist[neighbor] = distance + cost
            heappush(queue, (dist[neighbor], neighbor))
            prev[neighbor] = node

if prev[n] == -1:
    print(-1)
else:
    path = [n]
    while path[-1] != 1:
        path.append(prev[path[-1]])

    print(*path[::-1])
