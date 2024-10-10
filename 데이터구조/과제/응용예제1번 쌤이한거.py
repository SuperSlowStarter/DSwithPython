import random
import math

class Node:
    def __init__(self, inputData):
        self.data = inputData
        self.link = None

def create_storelists(store):
    global head, current, prev
    new_node = Node(store)

    x, y = new_node.data[1], new_node.data[2]
    distance = math.sqrt(x**2 + y**2)

    if head is None:
        head = new_node
        head.link = head
    else:
        current = head
        prev = None

        while True:
            current_x, current_y = current.data[1], current.data[2]
            current_distance = math.sqrt(current_x**2 + current_y**2)

            if distance < current_distance:
                if prev is None:
                    new_node.link = head
                    
                    last = head
                    while last.link is not head:
                        last = last.link
                    last.link = new_node
                    head = new_node
                else:
                    new_node.link = current
                    prev.link = new_node
                return
            prev = current
            current = current.link

            if current == head:
                break

        prev.link = new_node
        new_node.link = head

def print_stores():
    global head
    if head is None:
        return
    current = head
    while True:
        x, y = current.data[1], current.data[2]
        distance = math.sqrt(x**2 + y**2)
        print(f"{current.data[0]} 편의점, 거리: {distance:.3f}")
        current = current.link
        if current == head:
            break

head, current, prev = None, None, None

if __name__ == "__main__":
    stores = []
    store_names = [chr(i) for i in range (ord('A'), ord('K'))]

    for name in store_names:
        stores.append((name, random.randint(1, 100), random.randint(1, 100)))

    for store in stores:
        create_storelists(store)

    print_stores()