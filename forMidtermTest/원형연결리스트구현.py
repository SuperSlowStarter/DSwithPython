class Node():
    def __init__(self):
        self.data = None
        self.link = None


head, current, pre = None, None, None
dataArray = ["다혀","정여","즈위","산자","지호"]

if __name__ == "__main__": #시작노드 만들기
    node = Node() #노드만들고
    node.data = dataArray[0] #데이터넣어주고
    head = node #링크가져오기
    node.link = head #원형만들어주고

    for data in dataArray[1:]:
        prev = node #프레브땡겨오기
        node = Node() #노드만들고
        node.data = data #데이터
        prev.link = node #링크가져오기
        node.link = head #원형만들기