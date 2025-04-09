#set() 함수
-고유한 item 들의 정렬되지 않은 모음
-선어니 중괄호 {} 내부에 쉼표(,) 로 구분하여 item 나열
-slicing operation 을 통해 접근불가
-변경 가능한 아이템등 가질 수 없음
-아이템 추가, 제거 가능

#all
-반복 가능한 자료형의 모든 요소가 True 이면 True를 반환하고, 하나라도 False가 있으면 False를 반환
s = {1, 2, 3}
print(all(s)) #True -> 모든 값이 0이 아닌 정수
s2 = {1, 0, 3}
print(all(s2)) #False -> 0이 포함돼 있으니까

#any
-반복 가능한 자료형(set, list, tuple 등) 요소 중 하나라도 True이면 True를 반환하고,
모두 False이면 False를 반환하는 함수야.
s = {0, 0, 3}
print(any(s))  # True -> 3이 True니까


#enumerate()
-반복 가능한 객체를 인덱스와 함께 순회할 수 있게 해주는 함수
-인덱스와 값을 튜플 형태로 반환
-enumerate(iterable, start=0)
fruits = ["사과", "바나나", "딸기"]
for idx, fruit in enumerate(fruits):
  print(idx, fruit)

#difference()
-a.difference(b)는 집합 a에서 b에 있는 요소를 뺀 나머지를 반환 즉 a-b
a = {1, 2, 3, 4, 5}
b = {3, 4, 5}
result = a.difference(b)
print(result) #{1, 2, 3}

a = {10, 20 ,30}
b = {20, 40}
print(a-b)  #{10, 30}

#difference.update()
-a.difference_update(b)는 a에서 b와 겹치는 요소를 제거해서 a자체를 바꾼다.
-반환값은  없다.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5}
a.difference_update(b)
print(a)  # {1, 2, 3}

x = {10, 20, 30, 40}
y = {20, 50}
result = x.difference_update(y)
print(result)  # 출력: None (반환값 없음)
print(x)       # 출력: {10, 30, 40}

#discard()
-set.discard(x): 집합에서 요소 x를 제거
-x가 없으면 그냥 넘어가고 에러가 나지 않음
s = {1, 2, 3, 4}
s.discard(3)
print(s)  #{1, 2, 3}

s = {1, 2, 4}
s.discard(5)
print(s)  #{1, 2, 4}  오류 안남

# intersection()
-두개 이상의 집합에서 공통으로 존재하는요소만 뽑아낼 때
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.intersection(b)
print(result)  # 출력: {3, 4}

a = {1, 2, 3}
b = {2, 3, 4}
c = {0, 2, 3}
result = a.intersection(b, c)
print(result)  # 출력: {2, 3}

# intersection_update()
-교집합만 남기고, 원래 집합을 업데이트(변경)하는 함수
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)  #{3, 4}

# isdisjoint()
-두 집합(set)이 공통 요소를 하나도 안 가질 때 True 를 반환
-즉 서로소인지 확인하는 함수
-문법: set1.isdisjoint(set2)
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))  #True

a = {1, 2, 3}
b = {3, 4, 5}
print(a.isdisjoint(b))  # 출력: False

# issubset()
-집합 a가 집합 b의 부분 집합인지 확인
-즉 a의 모든 원소가 b에도 다 들어 있다면 True를 반환
-문법: a.issubset(b)
a = {1, 2}
b = {1,2 ,3, 4}
print(a.issubset(b))  #True

# issuperset()
-집합 a가 집합 b의 상위 집합인지 확인하는 함수
-즉, b의 모든 원소가 a에 다 들어있으면 True를 반환
-문법: a.issuperset(b)
a = {1, 2, 3, 4}
b = {2, 3}
print(a.issuprtset(b))  #True

# pop()
-집합에서 임의의 원소 하나를 제거하고 반환
-집합은 순서가 없기 때문에, 어떤 값이 나올지 예측 불가능
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print("꺼낸 값:", item)  # 꺼낸 값: banana
print("남은 집합:", fruits)  # {'apple', 'cherry}

# remove()
-집합에서 특정 원소를 제거할 때
-문법: set.remove(값)
-제거하려는 값이 집합에 없으면 에러발생
num = {1, 2, 3, 4}
num.remove(3)
print(num)  #{1, 2, 4}

# symmetric_difference()
-두 집합 간의 서로 다른 요소들만 모아서 반환
-즉, a에는 있지만 b에는 없고, b에는 있지만 a에는 없는 요소들
-문법:set1.symmetric_difference(set2)
a = {1, 2, 3}
b = {3, 4, 5}
result = a.symmetric_difference(b)
print(result)  #{1, 2, 4, 5}

#union()
-두 집합을 합친 것을 반환
-중복 없이 모든 요소를 합친 집합
a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print(result)  #{1, 2, 3, 4, 5}