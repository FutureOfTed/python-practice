import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

if n == len(a):
    print(min(a), max(a))
else:
    print(TypeError)
