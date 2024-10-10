# 초기 튜플 리스트 생성
initial_friends_tuple = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

# 친구 추가 함수
def add_friend(friends_tuple, new_friend, counts):
    inserted = False #false인 bool생성
    for i in range(len(friends_tuple)):
        # 새로운 친구의 카톡 횟수가 더 크면 해당 위치에 삽입
        if counts > friends_tuple[i][1]:
            friends_tuple.insert(i, (new_friend, counts))
            inserted = True
            break
    # 새로운 친구가 가장 적은 횟수를 가지고 있다면 리스트의 끝에 추가
    if not inserted:
        friends_tuple.append((new_friend, counts))

    return friends_tuple

# 친구 이름과 인원수 입력. 숫자가 아닐시 에러 #
while True:
    input_friend = input("추가할 친구--> ")
    try:
        katok_count = int(input("카톡 횟수--> "))
        initial_friends_tuple = add_friend(initial_friends_tuple, input_friend, katok_count)
        print(initial_friends_tuple)
    except ValueError:
        print("제대로된 숫자를 입력하시오.")
