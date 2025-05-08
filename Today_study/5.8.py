# Bag(가방) ADT 예제
# Bag ADT (비어있는 가방 만들고, 항목 추가, 삭제, 포함여부, 개수)
myBag = []

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    if e in bag:
        bag.remove(e)

def contains(bag, e):
    return e in bag

def count(bag):
    return len(bag)

# 사용 예시
insert(myBag, '사과')
insert(myBag, '바나나')
print(myBag)
print(contains(myBag, '사과'))
remove(myBag, '사과')
print(myBag)
print(count(myBag))

# 스택 ADT 예제
top = []

def isEmpty():
    return len(top) == 0

def push(item):
    top.append(item)

def pop():
    if not isEmpty():
        return top.pop(-1)

def peek():
    if not isEmpty():
        return top[-1]

def size():
    return len(top)

def clear():
    global top
    top = []

# 사용 예시
push(1)
push(2)
print(pop())   # 2
print(peek())  # 1
print(size())  # 1

# 큐 ADT 예제
items = []

def isEmpty():
    return len(items) == 0

def enqueue(item):
    items.append(item)

def dequeue():
    if not isEmpty():
        return items.pop(0)

def peek():
    if not isEmpty():
        return items[0]

def size():
    return len(items)

def clear():
    global items
    items = []

# 사용 예시
enqueue(10)
enqueue(20)
print(dequeue())  # 10
print(peek())     # 20
