import sys

n, m = map(int, sys.stdin.readline().split())

n_list = []

for i in range(1, n+1):
    n_list.append(i)

if 1 <= n <= 100 and 1 <= m <= 100:
    for a in range(m):
        i, j = map(int, sys.stdin.readline().split())
        if 1 <= i <= j <= n:
            n_list[i-1:j] = reversed(n_list[i-1:j])

    print(' '.join(map(str, n_list)))