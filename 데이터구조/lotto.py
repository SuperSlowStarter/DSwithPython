import random

def create_lotto_numbers (count) :
    lotto_numbers = []
    for i in range(count):
        numbers = set()
        while len(numbers) < 6:
            numbers.add(random.randint(1,45)) #set은 순서가 없으니까 add로 해야지
        lotto_numbers.append(numbers)
    return lotto_numbers

print("** 로또 번호를 생성합니다!! **")
count = int(input("몇 번을 뽑으까요?")) #parseint
lottos = create_lotto_numbers(count)
for i in range (count):
    print("자동번호--> " + str(lottos[i]))
    
