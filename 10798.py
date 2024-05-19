# 각 세로 줄에 대한 리스트 만들고 요소 추가

v = []
max = 0

for i in range(5):
    line = list(input(""))
    v.append(line)
    if max <= len(v[i]):
        max = len(v[i])

for i in range(max):
    for j in range(5):
        try:
            print(v[j][i], end='')
        except IndexError:
            continue
