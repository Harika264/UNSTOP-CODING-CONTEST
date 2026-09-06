import sys

input = sys.stdin.buffer.readline

n = int(input())

LOG = (n).bit_length()

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# depth[u] = number of edges from root to u
# dist[u] = total years from root to u
depth = [0] * (n + 1)
dist = [0] * (n + 1)

# up[j][u] = 2^j-th ancestor of u
up = [[0] * (n + 1) for _ in range(LOG)]

# Build parent/depth/dist using iterative DFS
stack = [1]
parent = [0] * (n + 1)
parent[1] = 0

while stack:
    u = stack.pop()

    for v, w in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        depth[v] = depth[u] + 1
        dist[v] = dist[u] + w
        stack.append(v)

# First ancestor
for u in range(1, n + 1):
    up[0][u] = parent[u]

# Binary lifting table
for j in range(1, LOG):
    for u in range(1, n + 1):
        up[j][u] = up[j - 1][up[j - 1][u]]


def lca(a, b):
    # Make a and b at the same depth
    if depth[a] < depth[b]:
        a, b = b, a

    difference = depth[a] - depth[b]

    for j in range(LOG):
        if difference & (1 << j):
            a = up[j][a]

    if a == b:
        return a

    # Move both nodes upward
    for j in range(LOG - 1, -1, -1):
        if up[j][a] != up[j][b]:
            a = up[j][a]
            b = up[j][b]

    return up[0][a]


q = int(input())

output = []

for _ in range(q):
    x, y = map(int, input().split())

    ancestor = lca(x, y)

    # Total years along the path
    years = dist[x] + dist[y] - 2 * dist[ancestor]

    # Number of rulers on the path
    count = depth[x] + depth[y] - 2 * depth[ancestor] + 1

    output.append(str(years) + " " + str(count))

sys.stdout.write("\n".join(output))
