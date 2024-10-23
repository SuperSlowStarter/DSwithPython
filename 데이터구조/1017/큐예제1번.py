from collections import deque

class RestaurantQueue:
    def __init__(self):
        self.queue=deque()
    def add_customer(self, customer):
        self.queue.append(customer)

    def enter_restaurant(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"{customer} 님이 식당에 들어가십니다.")
        else:
            print("대기줄에 손님이 없습니다.")

    def display_queue(self):
        if self.queue:
            print("현재 대기줄 상태: ", list(self.queue))
        else:
            print("대기줄이 비어 있습니다.")

def main():
    restaurant_queue = RestaurantQueue()
    customers = ["정국", "비", "지민", "진", "슈가"]
    for customer in customers:
        restaurant_queue.add_customer(customer)
    restaurant_queue.display_queue()

    while restaurant_queue.queue:
        restaurant_queue.enter_restaurant()
        restaurant_queue.display_queue()

        print("식당영업종료!")

if __name__ == "__main__":
    main()