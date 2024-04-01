# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다.
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

import sys

n, k = map(int, sys.stdin.readline().split())

def a_divisors(n):
    divisors = []
    for a in range(1, n + 1):
        if n % a == 0:
            divisors.append(a)
    return divisors

if len(a_divisors(n)) >= k:
    print(a_divisors(n))
else:
    print(0)