import sys

input = sys.stdin.buffer.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges by cost
edges.sort()

# DSU / Union-Find
parent = list(range(n + 1))
size = [1] * (n + 1)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    # Union by size
    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]

    return True


total_cost = 0
edges_used = 0

for w, u, v in edges:
    if union(u, v):
        total_cost += w
        edges_used += 1

        # MST needs exactly n-1 edges
        if edges_used == n - 1:
            break

# If we couldn't connect all n nodes
if edges_used != n - 1:
    print(-1)
else:
    print(total_cost)
