import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
h = data[1:1 + n]

answer = [0] * n
stack = []

# Traverse from right to left
for i in range(n - 1, -1, -1):

    # Remove towers that are not strictly taller
    while stack and h[stack[-1]] <= h[i]:
        stack.pop()

    if stack:
        # First taller tower to the right
        answer[i] = stack[-1] - i
    else:
        # No taller tower: all remaining towers are visible
        answer[i] = n - 1 - i

    stack.append(i)

print(*answer)
