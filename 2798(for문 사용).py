import sys

n, m = map(int, sys.stdin.readline().split())

if 3 <= n <= 100 and 10 <= m <= 300000:
    cards = list(map(int, sys.stdin.readline().split()))

    cards_sum = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                sum = int(cards[i]) + int(cards[j]) + int(cards[k])

                if sum <= m:
                    cards_sum.append(sum)

print(max(cards_sum))
