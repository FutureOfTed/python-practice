import sys

a, b = map(int, sys.stdin.readline().split())

if a >= 1 and b <= 10000:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
else:
    TypeError
