#Dictionary
'''
-키(key)와 값(value) 쌍으로 이루어진 자료형
-중괄호 {}를 사용해서 만듦
-각 키는 유일해야함
my_dict = {'name': 'Jack', 'age': 26}
my_dict['age']= 27
print(my_dict)
my_dict['add'] = 'Dt'
print(my_dict)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4)) # 키가 4인 항목을 꺼내서 삭제
print(squares)
print(squares.popitem()) #딕셔너리 마지막에 추가된 항목을 삭제 / 반환값은 튜플형태로 도출
squares.clear()
'''

# Dictionary 함수정리

#clear(): 딕셔너리의 모든 항목을 전부 삭제
scores = {"수학": 90, "영어": 85, "과학": 95}
scores.clear()
print(scores) # {}

#copy(): 딕셔너리를 복사해서 새로운 딕셔너리를 만드는 함수 / 원본과는 독립적인 복사본을 만듦 / new딕셔너리 = 딕셔너리.copy()
original = {"이름": "우빈", "나이": 25}
cloned = original.copy()
cloned["나이"] = 30
print("original", original) #{'나이': '우빈', '나이':25}
print("cloned", cloned) #{'이름': '우빈', '나이':30}

#fromkeys(seq[, v]): 리스트나 튜플 등 반복 가능한 값을 사용해서, 키만 있는 딕셔너리를 생성하는 메서드
'''-각 키에 대해 같은 값을 지정할 수 있음
-value를 생략하면 기본값은 None'''
keys = ["name", "age", "job"]
new_dict = dict.fromkeys(keys)
print(new_dict) #{'name': None, 'age': None, 'job': None}

#get(key[,default]): 딕셔너리에서 키에 해당하는 값을 가져오는 함수 /dict.get(키[, 기본값])
person = {"이름": "우빈", "나이": 25}
print(person.get("이름")) #우빈
print(person.get("직업")) #None
print(person.get("직업", "정보 없음")) #정보 없음

#item(): 딕셔너리의 모든 (키, 값)쌍을 튜플 형태로 반환해주는 함수
student = {"이름": "우빈", "점수": 95}
for key, value in student.items():
    print(f"{key}: {value}") #이름 : 우빈, 점수 : 95

#keys(): 딕셔너리의 모든 키만 모아서 반환하는 함수
student = {"이름": "우빈", "점수": 95}
print(student.keys()) # dict_keys(['이름', '점수'])
for key in student.keys():
    print(key)  #이름 점수

#pop(key[,d]: 특정 키에 해당하는 값을 꺼내면서 해당 키-값 쌍을 삭제 즉 꺼내고 동시에 제거
student = {"이름": "우빈", "점수": 95}
score = student.pop("점수")
print(score)  # 95
print(student) # {'이름': '우빈}
# 존재 여부를 모르는 키를 안전하게 꺼내고 싶을 때

#popitem(): 마지막에 추가된 key-value 쌍을 꺼내서 삭제하는 함수
fruits = {"apple"}: 1000, "banana": 1200, "melon": 1500}
item = fruits.popitem()
print(item)  #('melon': 1500)
print(fruits) #{'apple':1000, 'banana':1200}
#가장 마지막 값부터 하나씩 꺼내고 제거할 때

#setdefailt(key[, default]): 딕셔너리에 key가 있으면 해당 값을 반환하고 없으면 key를 추가하면서 default 값을 넣고 봔한
student = {"name": "우빈", "age": 20}
print(student.setdefault("name")) # 우빈
student = {"name": "우빈"}
print(student.setdefault("age", 25)) # 25
print(student) # {'name': '우빈', 'age': 25}

#update([other]): 다른 딕셔너리의 키-값 쌍을 현재 딕셔너리에 추가하거나 기존 키가 있으면 값을 덮어씀
info1 = {"name": "우빈", "age": 20}
info2 = {"job": "개발자"}
info1.update(info2)
print(info1) # {'name': '우빈', 'age': 20, 'job': '개발자'}

#values(): value 만 꺼내서 보여주는 함수
student = {"name": "우빈", "age": 20, "grade": "A"}
print(student.values()) # dict_values(['우빈', 20, '우빈'])

#all(): all(반복 가능한 객체)는 그 안의 모든 요소가 참이면 True, 하나라도 거짓이면 False
d = {1: "a", 2: "b"}
print(all(d)) # True
d = {0: "a", 2: "b"}
print(all(d))  # 0은 거짓 -->False

#any(): any(반복 가능한 객체)는 그 안에 하나라도 참이면 True 전부 거짓이면 False
print(any({0: 'a', 1: 'b'})) # 키에 1이 있어서 True
print(any({0: 'a'})) # 키가 0하나뿐 False

#len(): 객체의 길이를 반환
info = {"이름": "우빈", "나이": 20}
print(len(info)) # 2

#sorted(): 원본 데이터를 바꾸지 않고, 정렬된 새 리스트를 반환
sorted(iterable, key=None, reverse=True)
-iterable: 정렬할 대상
-key: 정렬 기준을 설정하는 함수
-reverse: True면 내림차순, False 면 오름차순 (기본값: False)
words = ['banana', 'apple', 'cherry']
print(sorted(words, key=len)) #['apple', 'banana', 'cherry']