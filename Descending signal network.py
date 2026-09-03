import sys

input = sys.stdin.buffer.readline

n = int(input())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

d = list(map(int, input().split()))

# Root tree at 0
parent = [-1] * n
pweight = [0] * n
order = [0]

for u in order:
    for v, w in graph[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        pweight[v] = w
        order.append(v)

# down[v] = contribution from the v-side when crossing
# edge (v,parent[v]) toward the parent.
down = d[:]

for u in reversed(order):
    if parent[u] == -1:
        continue

    pw = pweight[u]
    total = d[u]

    for v, w in graph[u]:
        if parent[v] == u and w > pw:
            total += down[v]

    down[u] = total

# up[u] = contribution coming from the parent side,
# when reaching u.
up = [0] * n

answer = 0

for u in order:

    # Every direction entering u:
    # (edge weight, contribution, neighbor)
    items = []

    if parent[u] != -1:
        items.append((pweight[u], up[u], parent[u]))

    for v, w in graph[u]:
        if parent[v] == u:
            items.append((w, down[v], v))

    # For hub u, every adjacent direction is valid because
    # there is only one edge.
    total = d[u]

    for w, val, v in items:
        total += val

    answer = max(answer, total)

    # Sort by edge weight descending.
    items.sort(reverse=True)

    # For each child, calculate the contribution from all
    # directions whose edge weight is STRICTLY greater.
    prefix = d[u]
    j = 0

    while j < len(items):
        w = items[j][0]

        k = j

        # Find all edges with the same weight.
        while k < len(items) and items[k][0] == w:
            k += 1

        # At this point prefix contains:
        # d[u] + all contributions with weight > w.

        for t in range(j, k):
            _, _, v = items[t]

            # Only children need an 'up' value.
            if parent[v] == u:
                up[v] = prefix

        # Add this weight group for smaller weights.
        for t in range(j, k):
            prefix += items[t][1]

        j = k

print(answer)
