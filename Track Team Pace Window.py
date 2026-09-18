from collections import deque

def solve():
    n, L = map(int, input().split())
    a = list(map(int, input().split()))

    max_dq = deque()
    min_dq = deque()

    left = 0
    answer = 0

    for right in range(n):
        # Maintain decreasing deque for maximum
        while max_dq and a[max_dq[-1]] <= a[right]:
            max_dq.pop()
        max_dq.append(right)

        # Maintain increasing deque for minimum
        while min_dq and a[min_dq[-1]] >= a[right]:
            min_dq.pop()
        min_dq.append(right)

        # Shrink window if max - min is too large
        while a[max_dq[0]] - a[min_dq[0]] > L:
            if max_dq[0] == left:
                max_dq.popleft()

            if min_dq[0] == left:
                min_dq.popleft()

            left += 1

        answer = max(answer, right - left + 1)

    print(answer)


if __name__ == "__main__":
    solve()
