import sys

input = sys.stdin.buffer.readline
MAX_BIT = 19

# Maximum number of trie nodes:
# N * (MAX_BIT + 1) + 1
MAX_NODES = 100000 * 21 + 5

left = [0] * MAX_NODES
right = [0] * MAX_NODES
count = [0] * MAX_NODES

nodes = 0


def insert(previous_root, value):
    global nodes

    new_root = nodes + 1
    nodes += 1

    left[new_root] = left[previous_root]
    right[new_root] = right[previous_root]
    count[new_root] = count[previous_root] + 1

    old_node = previous_root
    new_node = new_root

    for bit in range(MAX_BIT, -1, -1):
        b = (value >> bit) & 1

        if b == 0:
            old_child = left[old_node]

            new_child = nodes + 1
            nodes += 1

            left[new_child] = left[old_child]
            right[new_child] = right[old_child]
            count[new_child] = count[old_child] + 1

            left[new_node] = new_child

        else:
            old_child = right[old_node]

            new_child = nodes + 1
            nodes += 1

            left[new_child] = left[old_child]
            right[new_child] = right[old_child]
            count[new_child] = count[old_child] + 1

            right[new_node] = new_child

        old_node = old_child
        new_node = new_child

    return new_root


def max_xor(root_r, root_l, x):
    """
    Find maximum (value XOR x) among values
    occurring in prefix r but not prefix l.
    """

    answer = 0

    a = root_r
    b = root_l

    for bit in range(MAX_BIT, -1, -1):
        xbit = (x >> bit) & 1

        # To maximize XOR, we prefer the opposite bit.
        if xbit == 0:
            preferred_r = right[a]
            preferred_l = right[b]

            if count[preferred_r] - count[preferred_l] > 0:
                answer |= (1 << bit)
                a = preferred_r
                b = preferred_l
            else:
                a = left[a]
                b = left[b]

        else:
            preferred_r = left[a]
            preferred_l = left[b]

            if count[preferred_r] - count[preferred_l] > 0:
                answer |= (1 << bit)
                a = preferred_r
                b = preferred_l
            else:
                a = right[a]
                b = right[b]

    return answer



N = int(input())

arr = list(map(int, input().split()))

Q = int(input())

roots = [0] * (N + 1)

for i in range(1, N + 1):
    roots[i] = insert(roots[i - 1], arr[i - 1])




output = []

for _ in range(Q):
    l, r, x = map(int, input().split())

    
    result = max_xor(roots[r], roots[l - 1], x)

    output.append(str(result))

sys.stdout.write("\n".join(output))
