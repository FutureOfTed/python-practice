# n = 정수의 개수
# a = 정수들의 모임
# v = 정수 v

import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
v = int(input())

print(a.count(v))