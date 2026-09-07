import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline

    n, m, k, src, dst = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    INF = 10**30

    # dist[node][used_tokens]
    dist = [[INF] * (k + 1) for _ in range(n + 1)]

    dist[src][0] = 0

    # (cost, node, used_tokens)
    pq = [(0, src, 0)]

    while pq:
        cost, u, used = heapq.heappop(pq)

        if cost != dist[u][used]:
            continue

        if u == dst:
            print(cost)
            return

        for v, w in graph[u]:

            # Option 1: Travel normally
            new_cost = cost + w

            if new_cost < dist[v][used]:
                dist[v][used] = new_cost
                heapq.heappush(pq, (new_cost, v, used))

            # Option 2: Use a free-pass token
            if used < k:
                new_cost = cost

                if new_cost < dist[v][used + 1]:
                    dist[v][used + 1] = new_cost
                    heapq.heappush(pq, (new_cost, v, used + 1))

    # Destination cannot be reached
    print(-1)


if __name__ == "__main__":
    solve()
