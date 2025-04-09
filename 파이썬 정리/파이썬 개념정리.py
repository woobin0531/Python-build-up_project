#number data type
"""
-int, float, complex
 float: 소수점 이하 15자리까지 정확도 보장
-instance(): 주어진 값이 특정 클래스에 속하는지를 확인
 instance(값, 자료형)
 값: 확인하려는 값, 자료형: 확인할 타입 ex) int, str,
 결과는 "True" 또는 "False" 를 반환
-Decimal(소수)는 유한한 자리수까지 절삭되어 저장
 내장함수인 decimal을 사용하면 더 정확한 값으로 계산
  """

#List
"""
-여러 요소를 한번에 작업할 수 있는 데이터 유형
-각 요소에 순차적으로 접근할 수 있음
 인덱스는 0부터 시작하며, 정수만 가능함
 인덱스를 음수로 부여하면 끝에서부터 접근
 slicing operator를 사용 지원
-요소를 변경할 수 있음
-요소를 추가할 수 있음
-list 간의 결합/연결 지원
-list를 반복 수행 지원
ex)
odd = [1, 3, 5]

odd[0] = 0  # 0번째를 1-->0으로 바꾸는 법
odd[1:3] = [2,4] # 슬라이싱은 시작과 끝(-1)
print(odd)
odd[3:5] = [-5, -2]  #이렇게 추가도 가능
print(odd)
odd.append(7) # 맨 끝 인덱스에 추가 /하나의 아이템 추가
print(odd)
odd.extend([9, 11, 13]) #묶어서 들어갈 수도 있구나. 들어갈 땐 대괄호([]) 묶어서 / 여러 개의 아이템 추가 
print(odd) 
odd.insert(0,10) # 0 번째 자리에 10 추가 / 특정 위치에 아이템 추가
print(odd)
print(odd + [9, 7, 5])  # 중복가능이네? 
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list.remove('p')
print(my_list)
print(my_list.pop(1)) #pop:특정 인덱스 제거 
print(my_list)
print(my_list.pop())  #지정 않으면 마지막요소 꺼냄
my_list.clear()
print(my_list)  #list 전체 제거"""

# List 함수 정리

# append() : 리스트 맨 뒤에 값을 추가하는 함수
guest_list = ["우빈", "수아"]
guest_list.append("현우")
print(guest_list)  # ['우빈', '수아', '현우']

# extend() : 리스트에 여러 개의 항목을 한꺼번에 추가
guest_list = ["우빈", "수아"]
new_guests = ["현우", "지민"]
guest_list.extend(new_guests)
print(guest_list) #['우빈', '수아', '현우', '지민']

#insert() : 리스트의 원하는 위치에 값을 삽입 / 리스트.insert(인덱스, 값) / 인덱스가 리스트보다 크면 끝에 추가
guest_list = ["우빈", "수아", "현우"]
guest_list.insert(0, "VIP손님")
print(guest_list)  # ['VIP손님', '우빈', '수아', '현우']

#remove() : 리스트에 지정한 값을 찾아서 삭제 / 리스트.remove(값)
guest_list = ["우빈", "현우", "수아", "현우"]
guest_list.remove("현우")
print(guest_list)  # ['우빈', '수아', '현우']

#pop() : 리스트에서 값을 꺼내고 삭제하는 함수 / 리스트.pop(인덱스)
guest_list = ["우빈", "수아", "현우"]
last_guest = guest_list.pop()
print(last_guest)  #'현우'
print(guest_list)  # ['우빈', '수아']

#clear() : 리스트 안에 있는 모든 요소를 한 번에 삭제 / 리스트는 남고, 안의 값들만 사라짐
guest_list = ["우빈", "수아", "현우"]
guest_list.clear()
print(guest_list)  # []

#index() : 리스트에서 특정 값이 처음 등장하는 위치를 반환
guest_list = ["우빈", "수아", "현우", "수아"]
pos = guest_list.index("수아")
print(pos)  # 1

#count() : 리스트 안에서 특정 값이 등장한 횟수를 반환 / 숫자도 가능
guest_list = ["우빈", "수아", "현우", "수아", "수아"]
print(guest_list.count("수아")   # 3

#sort() : 리스트의 값을 오름차순으로 정렬 숫자면 숫자크기 문자열이면 알파벳 순서
scores = [50, 30, 90, 10]
scores.sort()
print(scores) # [10, 30, 50, 90]
리스트.sort(reverse=True)  #내림차순 정렬

#reverse() : 리스트의 순서를 거꾸로 뒤집어주는 함수 정렬이 아니라 현재 순서를 반대로 뒤집는 것
guests = ["우빈", "수아", "현우"]
guests.reverse()
print(guests)  #['현우', '수아', '우빈']

#copy() : 리스트를 그대로 복사해서 새로운 리스트를 만듬 / 새리스트 = 기존리스트.copy()
guest_list = ["우빈", "수아", "현우"]
backup_list = guest_list.copy()
print(backup_list)  #['우빈', '수아', '현우']

#Tuple
'''
-괄호 없이도 선언 가능하며, 쉼표 , 가 없으면 tuple로 인식하지 않음
-선언 이후에는 내부 아이템을 변경할 수 없지만, 재할당은 가능함
 내부 아이템이 list인 경우에는 변경 가능
-아이템만을 삭제할 수 없음
my_tuple = (4, 2, 3, [6, 5])
my_tuple[1]= 9 #item 변경불가능

my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0]= 9
print(my_tuple) # 내부아이템이 list인 경우 변경가능 
my_tuple = ('k', 'o', 'p', 'd')
print(my_tuple) #재할당은 가능
'''
#count(x) : x의 등장횟수를 반환
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # 3
print((5, 5, 5).count(5))  # 3

#index(x) : x가 처음 나타나는 인덱스를 반환
t = (10, 20, 30, 40)
print(t.index(30))  # 2
print((1, 2, 3, 2).index(2))  # 1
print(('a', 'b', 'c').index('c'))  # 2

#len(): 길이를 반환
print(len((1,2,3)))  # 3
print(len(()))  # 0
print(len(('apple', 'banana', 'cherry')))  # 3

#max(): 튜플에서 가장 큰 값을 반환
print(max((1, 5, 2)))  # 5
print(max(('a', 'c', 'b')))  # 'c'
print(max((10, 9, 11)))  # 11

#min(): 가장 작은 값을 반환
print(min((1, 5, 2)))  # 1
print(min(('a', 'c', 'b')))   # 'a'
print(min((10, 9, 11)))  # 9

#sum(): 모든 숫자 요소의 합을 반환
print(sum((1, 2, 3)))   # 6
print(sum((5, 5, 5, 5)))  # 20
print(sum((100,)))  #100

#sorted(): 튜플을 정렬된 리스트로 반환(튜플 자체는 변하지 않음)
print(sorted((3, 1, 2)))  # [1, 2, 3]
print(sorted(('b', 'c', 'a')))  # ['a', 'b', 'c']


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

# random 함수


#random.seed()
-랜덤값 생성을 위한 초기값(seed)을 설정.
-같은 seed 값을 주면 항상 같은 난수 결과
-주로 디버깅, 테스트, 예측 가능한 결과가 필요할 때 사용
import random
random.seed(42)
print(random.randint(1, 100))  # 82
print(random.random())  #0.63942...

#getstate(): 난수 생성기의 상태를 저장해서 나중에 똑같은 난수 시퀀스를 다시 생성할 수 있도록 해주는 함수
import random
state = random.getstate()
print(random.randint(1,100)) #23
random.setstate(state)
print(random.randint(1,100))  #23

#getrandbits(k): k비트 크기의 무작위 정수(0이상)를 생성하는 함수
import random
num = random.getrandbits(4)
print(num)  # 7

#random.randrange(): 지정된 범위 내에서 정수를 무작위로 하나 반환하는 함수
import random
print(random.ranfrange(10))  #0~9 중 하나 출력

#randint(): 지정된 두 정수 사이에서 난수를 무작위로 하나 반환/ 양쪽 끝 값 모두 포함
import random
print(random.randint(1, 10))  #1~10 중 하나 출력
dice = random.randint(1,6)
print(f"주사위의 눈: {dice}")

#choice(): 시퀸스 자료형에서 무작위로 하나의 요소를 선택해서 반환
import random
menu = ['김밥', '라면', '떡볶이', '순대']
lunch = random.choice(menu)
print(f"오늘 점심은 {lunch}")

#shuffle(): 리스트의 요소를 무작위로 섞어, 직접 리스트를 바로 변경하는 함수
import random
cards = ['A', '2', '3', '4', '5']
random.shuffle(cards)
print("셔플된 카드:", cards)

#sample(): w중복 없이, 주어진 시퀀스에서 원하는 개수만큼 랜덤하게 선택해서 리스트로 반환
import random
lotto = random.samle(ranfe(1, 46), 6)
print("로또 번호:", lotto)

#random():0.0 이상 1.0미만의 실수 중에서 무작위 숫자 하나를 반환하는 함수
import random
value = random.random()
print("랜덤 실수:", value)

#uniform(a, b): a이상 b이하의 실수 중에서 무작위로 하나를 리턴하는 함수
import random
value = random.uniform(1.0, 10.0)
print("1~10 사이의 랜덤 실수:", value)

#triangular(): low 이상 high 이하의 실수 중에서, mode(가장 자주 나올 값)에 가까운 숫자를 무작위로 반환하는 함수
import random
num = random.triangular(1, 100, 70)
print("70 근처가 잘 나오는 랜덤 값:", round(num, 2))

#betavariate(alpha, beta):0.0부터 1.0 사이의 실수 중에서, 베타 분포를 따르는 무작위 값을 반환해
import random
value = random.betavariate(2.0, 5.0)
print(f"0~1 사이의 베타 분포 값: {value:.3f}")

#expovariate(lambd):지수 분포를 따르는 랜덤한 실수를 반환
import random
arrival_time = random.expovariate(1/5)
print(f"다음 고객 도착까지 대기시간: {round(arrival_time, 2)}분")

#gammavariate(alpha, beta): 지수 분포의 일반화/ 연속적인 사건의 누적 시간이나 총 대기 시간을 모델링할 때 사용
import random
alpha = 3
beta = 10
waiting_time = random.gammavariate(alpha, beta)
print(f"총 대기 시간 예상: {round(waiting_time, 2)}초")

#gauss(mu, sigma): 데이터가 평균값을 중심으로 종모양으로 퍼지는 확률분포
import random
height = random.gauss(170, 5)
print(f"생성된 키: {round(height, 2)}cm")

#lognormvariate(): 로그정규분포, 어떤 변수 x가 정규분포를 따른다면 y = exp(x)가 로그 정규 분포를 따른다고 보는 분포
import random
value = random.lognormvariate(0, 1)
print("생성된 로그 정규값:", round(value, 3))

#normalvariate(): 정규분포를 따르는 난수를 생성해. 종모양으로 자연현상에서 자주 나옴
import random
x = random.normalvariate(0, 1)
print("정규분포 난수:", round(x, 3))

#vonmisesvariate(mu, kappa): 원형 데이터에서 사용하는 난수 생성함수
import random
import math
angle = random.vonmisesvariate(0, 1)
print("생성된 각도(라디안):", round(angle, 3))
print("각도(도):", round(math.degrees(angle), 2))

#paretovariate(alpha): 파레토 분포를 따르는 난수를 생성하는 함수
import random
print("파레토 난수:", random.paretovariate(2.0))

#weibullvariate(alpha, beta):weibull 분포를 따르는 난수를 생성하는 함수
import random
result = random.weibullvariate(1.5, 500)
print("Weibull 난수:", round(result, 2))
