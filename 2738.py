import sys

n, m = map(int, sys.stdin.readline().split())

if n <= 100 and m <= 100:
    a_list = []

    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        a_list.append(a)

    b_list = []

    for i in range(n):
        b = list(map(int, sys.stdin.readline().split()))
        b_list.append(b)

    s = []

    for i in range(n):
        c = []
        for j in range(m):
            if abs(a_list[i][j]) <= 100 and abs(b_list[i][j]) <= 100:
                c.append(a_list[i][j] + b_list[i][j])
        s.append(c)

    for c in s:
        print(' '.join(map(str, c)))
