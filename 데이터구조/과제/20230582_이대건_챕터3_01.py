# 초기 튜플 리스트 생성
initial_friends_tuple = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

# 친구 삽입 함수 add_friend
def add_friend(friends_tuple, new_friend, counts):
    # 삽입할 위치를 찾는 position을 -1로 초기화
    position = -1
    for i in range(len(friends_tuple)):
        if counts >= friends_tuple[i][1]:
            position = i #튜플의 첫 값부터 비교
            break

    # 삽입할 위치가 없으면 리스트 끝에 삽입
    if position == -1:
        position = len(friends_tuple)

    # None을 추가하여 새로운 친구를 위한 자리 마련
    friends_tuple.append(None)

    # position에 맞게 요소들 뒤로 이동
    for i in range(len(friends_tuple) - 1, position, -1):
        friends_tuple[i] = friends_tuple[i - 1]

    # 새로 입력받은 친구를 position에 삽입
    friends_tuple[position] = (new_friend, counts)

    return friends_tuple

# 친구 이름과 인원수 입력. 숫자가 아닐시 에러 처리
while True:
    input_friend = input("추가할 친구--> ")
    try:
        katok_count = int(input("카톡 횟수--> "))
        initial_friends_tuple = add_friend(initial_friends_tuple, input_friend, katok_count)
        print(initial_friends_tuple)
    except ValueError:
        print("제대로된 숫자를 입력하시오.")
