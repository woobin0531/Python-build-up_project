# 딕셔너리 키 리스트 만들기
# 아래 딕셔너리에서 모든 키(key)만 리스트로 만들어 출력하세요
fruit_prices = {"apple": 1000, "banana": 800, "orange": 1200}
print(list(fruit_prices.keys()))

# 딕셔너리 값 변경
# 아래 딕셔너리에서 "math" 과목의 점수를 95로 변경하세요.
scores = {"math": 80, "english": 90, "science": 85}
scores["math"] = 95
print(scores)

# 딕셔너리 항목 삭제
# 아래 딕셔너리에서 "cat" 항목을 삭제하세요.
animals = {"dog": "강아지", "cat": "고양이", "bird": "새"}
animals.pop("cat")
print(animals)

# 두 개의 리스트를 딕셔너리로 변환
# 아래 두 개의 리스트를 이용해, 과일 이름을 키로, 가격을 값으로 하는 딕셔너리를 생성하세요.
fruits = ["apple", "banana", "peach"]
prices = [3000, 2000, 4000]
fruit_dict = dict(zip(fruits, prices))
print(fruit_dict)

# 딕셔너리에서 값 기준으로 키 찾기
# 아래 딕셔너리에서 값이 1인 모든 키를 리스트로 만들어 출력하세요.
word_count = {'big': 1, 'good': 1, 'sky': 1, 'blue': 0, 'mouse': 1}
list_word = []
for word, count in word_count.items():
  if count == 1:
    list_word.append(word)
print(list_word)

# 딕셔너리 컴프리헨션 활용
# 1부터 5까지의 수를 키로 하고,각 키의 제곱을 값으로 하는 딕셔너리를
# 딕셔너리 컴프리헨션으로 한 줄에 만드세요
dict_a = {x: x**2 for x in range(1, 6)}
print(dict_a)

# setdefault와 defaultdict 활용
# 문자열 리스트가 주어졌을 때, 각 단어가 등장한 횟수를 세어 딕셔너리로 만드세요.
# 단, 키가 없을 때 자동으로 0으로 초기화하는 방법을 사용하세요.
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = {}
for word in words:
  count.setdefault(word, 0)
  count[word] += 1
print(count)

# 딕셔너리의 값에 리스트 저장 및 추가
# 학생별로 여러 과목의 점수를 저장하는 딕셔너리가 있습니다.
# 아래와 같이 데이터를 추가하는 코드를 작성하세요.
# 철수: 수학 90점, 영어 85점
# 영희: 수학 95점, 과학 100점
# (각 학생 이름을 키, 과목과 점수의 튜플을 값의 리스트로 저장
# 예: {'철수': [('수학', 90), ('영어', 85)], ...})
scores = {}

scores.setdefault("철수", []).append(('수학', 90))
scores['철수'].append(('영어', 85))

scores.setdefault('영희', []).append(('수학', 95))
scores['영희'].append(('과학', 100))
print(scores)

"""
scores = {}
if '철수' not in scores:
  scores['철수'] = []
scores['철수'].append(('수학', 90))
scores['철수'].append(('영어', 85))

if '영희' not in scores:
  scores['영희'] = []
scores['영희'].append(('수학', 95))
scores['영희'].append(('과학', 100))
print(scores)
"""

# 딕셔너리의 키와 값 동시 반복 및 평균 계산
# 아래 딕셔너리에서 for문을 사용해 학생별 점수를 출력하고,
# 전체 학생의 평균 점수를 마지막에 출력하세요.
data = {
    "철수": 98,
    "영희": 80,
    "순이": 100,
    "돌이": 70,
}

total = 0
count = 0

for name, score in data.items():
  print(f"{name} {score}")
  total += score
  count += 1

print("-"* 16)
avr = total // count
print(f"평균 {avr}")

# 집합 만들기와 자료형 확인
# 아래 리스트를 집합(set)으로 변환하고, 그 자료형(type)을 출력하세요.
numbers = [1, 2, 2, 3, 4]
set_num = set(numbers)
print(type(set_num))

# 집합에서 요소 제거
# 아래 집합에서 'banana'를 제거한 뒤 결과를 출력하세요.
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)

# 집합의 포함 여부 확인
# 아래 집합에 숫자 7이 포함되어 있는지 True/False로 출력하세요.
s = {3, 5, 7, 9}
print(7 in s)

# 두 집합의 합집합, 교집합, 차집합 구하기
# 아래 두 집합을 이용해
# ① 합집합
# ② 교집합
# ③ 첫 번째 집합에서 두 번째 집합을 뺀 차집합을 각각 구해 출력하세요.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# ① 합집합
union_1 = set1 | set2
print(union_1)
# ② 교집합
print(set1 & set2)
# ③
print(set1 - set2)

# 집합의 부분집합, 상위집합 판별
# 아래 두 집합에서
# ① set_a가 set_b의 부분집합인지
# ② set_b가 set_a의 상위집합인지를 각각 True/False로 출력하세요.
set_a = {2, 4}
set_b = {2, 4, 6, 8}

# 부분집합 판별
print(set_a.issubset(set_b))

# 상위집합 판별
print(set_b.issuperset(set_a))

# 집합의 대칭차집합 구하기
# 아래 두 집합에서
# 두 집합 중 하나에만 포함된 원소들의 집합(대칭차집합)을 구해 출력하세요.
x = {'apple', 'banana', 'cherry'}
y = {'banana', 'kiwi', 'grape'}

x_y_diff = x ^ y
print(x_y_diff)

# 여러 집합의 연산과 집합 메서드 활용
# 아래 세 집합이 있습니다.
# 세 집합의 모든 원소가 한 번씩만 포함된 집합(합집합)을 구하세요.
# 세 집합 모두에 공통으로 들어 있는 원소(교집합)를 구하세요.
# set_a에만 있고 set_b, set_c에는 없는 원소의 집합(차집합)을 구하세요.
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7}

print(set_a | set_b | set_c)
print(set_a & set_b & set_c)
print(set_a - (set_b | set_c))

# 집합을 이용한 아나그램 판별 함수 만들기
# 두 개의 단어가 주어졌을 때,
# 각 단어에 사용된 알파벳 종류가 정확히 같으면 True,
# 아니면 False를 반환하는 함수를 작성하세요.
# (단, 대소문자는 구분하지 않고, 알파벳 이외의 문자는 무시합니다.)
# 예시1
word1 = "Listen!"
word2 = "Silent"
# → True
# 예시2
word1 = "Python"
word2 = "Typhon"
# → True

import string

def a_set(word1, word2):
  w1 = set(i.lower() for i in word1 if i.isalpha())
  w2 = set(i.lower() for i in word2 if i.isalpha())
  return w1 == w2

print(a_set("Listen!", "Silent"))

# 집합을 활용한 데이터 중복 제거 및 정렬
# 아래와 같이 여러 번 등장하는 숫자가 있는 리스트가 있습니다.
# 이 리스트에서 중복을 제거하고,
# 남은 숫자들을 오름차순으로 정렬한 리스트로 만드세요.
nums = [5, 3, 8, 3, 1, 5, 9, 1, 2]
sorted_num = sorted(set(nums))
print(sorted_num)

# 랜덤 숫자 집합 만들기
# 1부터 10까지의 정수 중에서 서로 다른 숫자 3개를 랜덤하게 뽑아
# 집합(set)으로 만들어 출력하세요.
import random

nums = set(random.sample(range(1, 11), 3))
print(nums)

# 랜덤 알파벳 집합 생성
# 알파벳 소문자 중에서 5개를 랜덤하게 뽑아 집합(set)으로 만들고,
# 그 집합의 길이를 출력하세요
import random
import string

letters = set(random.sample(string.ascii_lowercase, 5))
print(letters)
print(len(letters))

# 랜덤 리스트에서 중복 제거
# 1부터 5까지의 숫자 중에서 10개를 랜덤하게 뽑아 리스트로 만들고
# 이 리스트에서 중복을 제거한 집합(set)을 출력하세요.
import random

a = [random.randint(1, 5) for i in range(10)]
print(a)
set_a = set(a)
print(set_a)

# 랜덤 실수 생성 및 반올림
# random 모듈을 사용하여 1 이상 100 미만의 실수(float)를 하나 생성하고
# 소수점 둘째 자리까지 반올림해서 출력하세요.
import random
a = random.uniform(1, 100)
print(round(a, 2))

# 리스트 섞기와 슬라이싱
# 1부터 10까지의 숫자로 이루어진 리스트를 랜덤하게 섞은 뒤
# 앞에서 3개만 출력하세요.
import random

a = list(range(1, 11))
random.shuffle(a)
b = a[:3]
print(b)

# 랜덤 추첨 프로그램
# 아래와 같이 10명의 이름이 들어 있는 리스트가 있습니다.
# 이 중에서 3명을 중복 없이 무작위로 뽑아 출력하는 코드를 작성하세요.
names = ['철수', '영희', '민수', '지민', '수진', '현우',
         '나영', '준호', '예린', '다은']
sample_names = random.sample(names, 3)
print(sample_names)