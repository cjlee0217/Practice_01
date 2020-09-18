## 연습문제 1 ##
gravity = [7,4,2,0,0,6,0,7,0] #상자들의 높이

fall_list = []
for i in range(0,len(gravity)):
    count = 0
    for j in range(i+1, len(gravity)):
        if gravity[i] > gravity[j]:
            count += 1
    fall_list.append(count)

print(max(fall_list))


## 연습문제 2 ##
def palindrome(sent):
    original = []
    for s in sent:
        if s ==" ":
            continue
        else:
            original.append(s)
    pal = []
    for i in range(len(original)-1,-1,-1):
        pal.append(original[i])
    return "".join(original) == "".join(pal)

sent = input("회문 입력: ")
print(palindrome(sent))


## 연습문제 3 ##
all_numbers = set(range(1,5001))
generator = set()

for n in range(1,5001):
    for d in str(n):
        n += int(d)
    generator.add(n)

self_num = all_numbers - generator

total = sum(self_num)
print(total)


## 연습문제 4 ##
count = 0
for n in range(1, 10000,1):
    for s in str(n):
        if s == '8':
            count += 1
print(count)