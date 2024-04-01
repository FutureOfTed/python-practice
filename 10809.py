# 1번째 줄에 단어 S가 주어짐 X
# 단어의 길이는 100을 넘지 않음 X
# 알파벳 소문자로만 이루어짐 X

s = input("")

s_list = list(s.lower())

all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = 0
j = 0

if len(s_list) <= 100:
    for i in range(len(all)):
        if all[i] in s_list:
            for j in range(len(s_list)):
                if all[i] == s_list[j]:
                    a = s_list.index(s_list[j])
            print(a)
        else:
            print(-1)
