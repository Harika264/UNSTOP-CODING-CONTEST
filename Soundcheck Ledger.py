import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
L = data[1]
a = data[2:2 + n]

max_q = deque()
min_q = deque()

left = 0
answer = 0

for right in range(n):

    # Maintain decreasing deque for maximum
    while max_q and a[max_q[-1]] <= a[right]:
        max_q.pop()
    max_q.append(right)

    # Maintain increasing deque for minimum
    while min_q and a[min_q[-1]] >= a[right]:
        min_q.pop()
    min_q.append(right)

    # Shrink window while max - min > L
    while a[max_q[0]] - a[min_q[0]] > L:

        if max_q[0] == left:
            max_q.popleft()

        if min_q[0] == left:
            min_q.popleft()

        left += 1

    answer = max(answer, right - left + 1)

print(answer)
