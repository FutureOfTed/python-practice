p = []

for i in range(1, 29):
    n = int(input())
    if 1 <= n <= 30:
        p.append(n)

students = []

for i in range(1, 31):
    students.append(i)

missing = []

# 미제출 학생 번호 꺼내서 missing 리스트에 요소 추가
for num in students:
    if num not in p:
        missing.append(num)

# missing 리스트 정렬 (낮은 숫자부터)
missing_students = sorted(missing)

print(missing[0])
print(missing[1])