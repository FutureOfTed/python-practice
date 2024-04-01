import sys

a, b = map(int, sys.stdin.readline().split())

if 0 < a < 10 and 0 < b < 10:
    print(a * b)
else:
    TypeError
