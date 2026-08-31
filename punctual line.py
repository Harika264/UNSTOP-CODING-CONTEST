import sys
import heapq

input = sys.stdin.buffer.readline

# Read n, m, S, D
n, m, S, D = map(int, input().split())

# Adjacency list
graph = [[] for _ in range(n + 1)]

# Read train services
for _ in range(m):
    u, v, first, freq, dur = map(int, input().split())
    graph[u].append((v, first, freq, dur))

# Earliest known arrival time at each station
INF = 10**30
dist = [INF] * (n + 1)

dist[S] = 0

# Priority queue: (arrival_time, station)
pq = [(0, S)]

while pq:
    current_time, u = heapq.heappop(pq)

    # Ignore outdated entry
    if current_time != dist[u]:
        continue

    # First time we remove D, it is optimal
    if u == D:
        print(current_time)
        sys.exit(0)

    for v, first, freq, dur in graph[u]:

        # Case 1: We arrive before or exactly when
        # the first train leaves.
        if current_time <= first:
            departure = first

        # Case 2: One-time special already left.
        elif freq == 0:
            continue

        # Case 3: Periodic train.
        else:
            # Need the smallest k such that:
            # first + k * freq >= current_time
            k = (current_time - first + freq - 1) // freq
            departure = first + k * freq

        # Arrival time at v
        arrival = departure + dur

        # Relax the edge
        if arrival < dist[v]:
            dist[v] = arrival
            heapq.heappush(pq, (arrival, v))

# Destination cannot be reached
print(-1)
