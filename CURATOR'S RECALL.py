import sys
from math import isqrt

input = sys.stdin.buffer.readline

n = int(input())
a = list(map(int, input().split()))

q = int(input())

queries = []

for i in range(q):
    l, r = map(int, input().split())
    # Convert to 0-based
    l -= 1
    r -= 1
    queries.append((l, r, i))

# Size of each Mo's block
block = isqrt(n) + 1

# Sort queries for Mo's algorithm
queries.sort(
    key=lambda x: (
        x[0] // block,
        x[1] if (x[0] // block) % 2 == 0 else -x[1]
    )
)

# Coordinate compression
# Artist IDs can be as large as 1e9.
values = sorted(set(a))
compressed = {value: i for i, value in enumerate(values)}

arr = [compressed[x] for x in a]

# Frequency of each artist in current range
freq = [0] * len(values)

# Current range
cur_l = 0
cur_r = -1

# Number of distinct artists
distinct = 0

answer = [0] * q

for l, r, idx in queries:

    # Expand/shrink left side
    while cur_l > l:
        cur_l -= 1
        x = arr[cur_l]

        if freq[x] == 0:
            distinct += 1

        freq[x] += 1

    while cur_l < l:
        x = arr[cur_l]
        freq[x] -= 1

        if freq[x] == 0:
            distinct -= 1

        cur_l += 1

    # Expand right side
    while cur_r < r:
        cur_r += 1
        x = arr[cur_r]

        if freq[x] == 0:
            distinct += 1

        freq[x] += 1

    # Shrink right side
    while cur_r > r:
        x = arr[cur_r]
        freq[x] -= 1

        if freq[x] == 0:
            distinct -= 1

        cur_r -= 1

    answer[idx] = distinct

sys.stdout.write("\n".join(map(str, answer)))
