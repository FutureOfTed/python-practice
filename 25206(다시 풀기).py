import sys

li = []
sum = 0
total = 0

for i in range(20):
    li.append(sys.stdin.readline().split())

    n = li[i][1]
    grade = li[i][2]

    if grade == "A+":
        grade = 4.5
    elif grade == "A0":
        grade = 4.0
    elif grade == "B+":
        grade = 3.5
    elif grade == "B0":
        grade = 3.0
    elif grade == "C+":
        grade = 2.5
    elif grade == "C0":
        grade = 2.0
    elif grade == "D+":
        grade = 1.5
    elif grade == "D0":
        grade = 1.0
    elif grade == "F":
        grade = 0.0
    elif grade == "P":
        continue
    else:
        TypeError
    sum += float(n) * float(grade)
    total += float(n)

average = sum / total

print(average)

# 전공평점 = 전공과목별 (학점 (= n) * 과목평점 (= grade))의 합 / 학점의 총합
# li[0] ~ li[19]
