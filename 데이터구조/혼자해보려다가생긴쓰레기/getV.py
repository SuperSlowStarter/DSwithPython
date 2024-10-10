import random

n = int(input("몇 개의 정수를 받으시겠습니까?? : "))
v = int(input("무슨 수를 찾으십니까? : "))
li=[]
count = 0

if n >= 1 or n <= 100 :
    for _ in range(n) :
        num = random.randint(1, 100)
        li.append(num)

for i in range(len(li)) :
    print(li[i], end=' ')


for key in range(n) :
    if li[key] == v:
        count += 1
    else :
        key += 1
        continue

print("\n")
print(count)