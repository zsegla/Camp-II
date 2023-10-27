# https://codeforces.com/problemset/problem/601/A



from collections import deque

def bfs(adj, n):
    vis = [0] * (n + 1)
    q = deque()
    q.append(1)
    vis[1] = 1
    dis = 0
    while q:
        size = len(q)
        while size > 0:
            node = q.popleft()
            size -= 1
            if node == n:
                return dis
            for i in adj[node]:
                if not vis[i]:
                    vis[i] = 1
                    q.append(i)
        dis += 1
    return -1

def main():
    n, m = map(int, input().split())
    adj1 = [[] for _ in range(n + 1)]
    edge = {}
    flag = 0
    for _ in range(m):
        u, v = map(int, input().split())
        if (u == 1 and v == n) or (u == n and v == 1):
            flag = 1
        if (u, v) not in edge:
            edge[(u, v)] = 0
        if (v, u) not in edge:
            edge[(v, u)] = 0
        edge[(u, v)] += 1
        edge[(v, u)] += 1
        adj1[u].append(v)
        adj1[v].append(u)
    
    if not flag:
        print(bfs(adj1, n))
    else:
        adj2 = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if (i, j) not in edge:
                    adj2[i].append(j)
                    adj2[j].append(i)
        
        print(bfs(adj2, n))

if __name__ == "__main__":
    main()
