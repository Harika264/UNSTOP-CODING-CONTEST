from collections import deque

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dq = deque()
    result = []

    for i in range(n):
        # Remove indices that are outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values from the back
        while dq and a[dq[-1]] <= a[i]:
            dq.pop()

        dq.append(i)

        # Window is complete
        if i >= k - 1:
            result.append(a[dq[0]])

    print(*result)


if __name__ == "__main__":
    solve()
