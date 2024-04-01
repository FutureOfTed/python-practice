n = input("")
a = list(n)
if 1 <= len(a) <= 100:
    b = len(a)
i = 0

if a[i] == a[-i-1]:
    while a[i] != a[-i-1]:
        i += 1
    print(1)
else:
    print(0)


#noon   4자리
#0123
#-4-3-2-1

#level
#01234
#-5-4-3-2-1

# 알파벳 개수 짝수 홀수 구분
#  0, -1 / 1, 8 / 2, 7 ....