import sys

input = sys.stdin.buffer.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# freq[r] = number of prefix sums seen with remainder r
freq = [0] * k

# Empty prefix sum has remainder 0
freq[0] = 1

prefix = 0
answer = 0

for x in a:
    prefix += x

    # Python's % gives a non-negative remainder for positive k
    rem = prefix % k

    # Every previous prefix with the same remainder
    # forms a valid subarray ending here.
    answer += freq[rem]

    freq[rem] += 1

print(answer)
