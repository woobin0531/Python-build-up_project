# 리스트의 합 구하기
# 주어진 리스트의 모든 숫자를 더한 값을 출력하세요.
numbers = [3, 7, 1, 9, 2]
print(sum(numbers))

# 특정 값 세기
# 아래 리스트에서 숫자 2가 몇 번 나오는지 세어 출력하세요.
nums = [2, 4, 2, 1, 3, 2, 5]
nums.count(2)

# 리스트 뒤집기
# 아래 리스트를 뒤집은 결과를 출력하세요.
data = [10, 20, 30, 40, 50]
print(data[::-1])

# 짝수만 추출하기
# 아래 리스트에서 짝수만 골라 새로운 리스트로 만들어 출력하세요.
nums = [4, 7, 2, 9, 12, 5, 8]
a = []
for i in nums:
  if i % 2 == 0:
    a.append(i)
print(a)

# 중복 제거 후 정렬
# 아래 리스트에서 중복된 값을 제거하고, 오름차순 정렬하여 출력하세요.
data = [3, 5, 1, 3, 2, 5, 4, 1]
set(data)

# 최대값과 최소값의 차이 구하기
# 아래 리스트에서 가장 큰 값과 가장 작은 값의 차이를 출력하세요.
scores = [88, 73, 92, 100, 67, 85]
print(max(scores)-min(scores))

# 2차원 리스트에서 특정 값 찾기
# 아래 2차원 리스트에서 숫자 7의 위치(행, 열 인덱스)를 찾아 출력하세요.
matrix = [
    [1, 3, 5],
    [4, 7, 9],
    [6, 2, 8]
]
for row in range(len(matrix)):
  for col in range(len(matrix[row])):
    if matrix[row][col] == 7:
      print(f"7의 위치는: ({row}, {col})")

matrix = [
    [1, 3, 5],
    [4, 7, 9],
    [6, 2, 8]
]
for row in range(len(matrix)):
  for cow in range(len(matrix[row])):
    if matrix[row][cow] == 7:
      print({row},{cow})

# 리스트에서 중복된 숫자만 모아 출력하기
# 아래 리스트에서 중복으로 등장하는 숫자만 모아, 중복 없이 출력하세요.
nums = [1, 3, 2, 3, 4, 2, 5, 1, 6]
# 결과 예시: [1, 2, 3]
a = []
for i in nums:
  if nums.count(i) > 1 and i not in a:
    a.append(i)
print(a)

# 문자열 길이 구하기
# 아래 문자열의 길이를 출력하세요.
text = "Hello, Python!"
print(len(text))

# 첫 글자와 마지막 글자 출력
# 아래 문자열에서 첫 글자와 마지막 글자를 출력하세요.
word = "Programming"
print(word[1], word[-1])

# 문자열 거꾸로 출력
# 아래 문자열을 거꾸로 출력하세요.
msg = "OpenAI"
print(msg[::-1])

# 단어 개수 세기
# 아래 문장에서 단어의 개수를 세어 출력하세요.
sentence = "Life is short, you need Python"
print(len(sentence))

# 모음만 골라서 출력
# 아래 문자열에서 모음(a, e, i, o, u)만 골라 출력하세요.
word = "Artificial Intelligence"
b = "aeiouAEIOU"
for i in a:
  if i in b:
    print(i, end="")

# 대소문자 뒤집기
# 아래 문자열에서 대문자는 소문자로, 소문자는 대문자로 바꿔 출력하세요.
text = "PyTHon iS FuN"
new_text = ""
for i in text:
  if i.islower():
    new_text += i.upper()
  elif i.isupper:
    new_text += i.lower()
print(new_text)

# 중복 문자 제거 (순서 유지)
# 아래 문자열에서 중복된 문자를 제거하되, 처음 나온 순서는 유지하세요.
text = "banana"
# 예: "ban"
new_text = ""
for i in text:
  if i not in new_text:
    new_text += i
  else:
    pass
print(new_text)

# 아래 튜플에서 첫 번째 요소를 출력하세요.
info = ("Alice", 25, "Seoul")
print(info[0])

# 아래 두 튜플을 연결(concatenate)하여 새로운 튜플을 만드세요.
a = (1, 2, 3)
b = (4, 5)
print(a+b)

# 아래 튜플에서 마지막 요소를 슬라이싱을 사용하여 튜플 형태로 출력하세요.
numbers = (10, 20, 30, 40, 50)
print(numbers[-1:]) # 튜플 형태로 출력하려면 [-1] 이아니라 [-1:]로 출력

# 튜플 언패킹
# 아래 튜플의 값을 각각 변수에 저장하고, 출력하세요.
person = ("Bob", 30, "Busan")
# name, age, city 에 각각 저장
name, age, city = person
print(name, age, city)

# 특정 값 포함 여부
# 아래 튜플에 숫자 7이 포함되어 있는지 확인하고 결과를 출력하세요.
nums = (3, 6, 9, 12, 15)
nums.count(7)

# 튜플 리스트 처리
# 아래 튜플 리스트에서 평균 점수가 80점 이상인 학생들 이름을 출력하세요.
students = [
    ("Anna", [85, 92, 78]),
    ("Ben", [70, 68, 75]),
    ("Clara", [90, 88, 95])
]

for i in students:
  name = i[0]
  score = i[1]
  a = sum(score)/len(score)
  if a >= 80:
    print(name)

# 중첩 튜플에서 최대값 찾기
# 아래 튜플에서 각 서브 튜플의 최대값을 찾아 새로운 튜플로 만드세요.
numbers = (
    (3, 8, 5),
    (1, 6, 9),
    (7, 2, 4)
)
# 결과 예시: (8, 9, 7)
a = []
for i in numbers:
  a += [max(i)]
print(a)

result = tuple(max(i) for i in numbers)
print(result)

# 튜플에서 요소 교환
# 아래 튜플에서 첫 번째 요소와 마지막 요소를 교환한 새로운 튜플을 만드세요.
data = (10, 20, 30, 40, 50)
# 결과 예시: (50, 20, 30, 40, 10)
data_list = list(data)
data_list[0], data_list[-1] = data_list[-1], data_list[0]
new_data = tuple(data_list)
print(new_data)

# 딕셔너리 값 접근
# 아래 딕셔너리에서 "age" 값을 출력하세요.
person = {"name": "Alice", "age": 25, "city": "Seoul"}
print(person["age"])

# 딕셔너리에 값 추가
# 아래 딕셔너리에 "email": "alice@example.com" 항목을 추가하세요.
person = {"name": "Alice", "age": 25}
person["email"]= "alice@example.com"
print(person)

# 딕셔너리 반복 출력
# 아래 딕셔너리의 모든 key와 value를 한 줄씩 출력하세요.
fruits = {"apple": 3, "banana": 5, "orange": 2}
for key, value in fruits.items():
  print(key)
  print(value)

# 값 기준으로 조건 출력하기
# 점수가 80점 이상인 학생들만 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
good_students = []
for key, value in scores.items():
  if value >= 80:
    good_students.append(key)
print(good_students)

# 딕셔너리에서 최대값 찾기
# 아래 딕셔너리에서 가장 점수가 높은 학생의 이름과 점수를 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
king_student = ""
king_score = 0
for name, score in scores.items():
  if score > king_score:
    king_score = score
    king_student = name
print(king_student, king_score)

# 값 업데이트
# 아래 딕셔너리에서 모든 학생의 점수에 +5점을 더해 업데이트하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
for name, score in scores.items():
  score += 5
  scores = score
  print(name,scores)

# 점수로 순위 매기기
# 아래 딕셔너리에서 점수를 기준으로 학생들을 내림차순으로 정렬해서 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
#sorted_scores = [scores for name, score in scores.items(), sorted(scores, key=lambda x: x[1])]
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for name, score in sorted_scores:
  print(f"{name}: {score}")

# 평균 점수 계산하기
# 아래와 같이 각 학생의 과목별 점수가 있을 때,
# 모든 학생의 평균 점수를 구해서 새로운 딕셔너리로 만들어 출력하세요.

students = {
    "Anna": [85, 90, 78],
    "Ben": [70, 75, 80],
    "Clara": [95, 92, 88]
}
ave_students = {}
for name, scores in students.items():
  #ave_students[name] = sum(scores)/len(scores)
  #print(ave_students)
  ave = sum(scores) / len(scores)
  ave_students[name] = round(ave, 2)  # round(숫자, 자릿수)
print(ave_students)                   #문자열(str), 리스트(list), 튜플(tuple) 등에 직접적으로 쓰면 오류

# 특정 조건에 맞는 키만 추출
# 아래 딕셔너리에서 이름이 A로 시작하는 학생만 뽑아서 새로운 딕셔너리를 만들어 출력하세요.
students = {
    "Anna": 85,
    "Ben": 77,
    "Alice": 92,
    "Clara": 88
}
start_a = {}

for name, score in students.items():
  if name.startswith("A"):
    start_a[name] = score
print(start_a)

# 중복 제거하기
# 아래 리스트에서 중복된 숫자를 제거하고 set으로 출력하세요.
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))

# 길이 구하기
# 아래 set의 요소 개수를 출력하세요.
fruits = {"apple", "banana", "cherry", "banana"}
len(fruits)

# 특정 요소 포함 여부 확인
# 아래 set에 "banana"가 있는지 확인하고,
# 있다면 "있음", 없으면 "없음"을 출력하세요.
fruits = {"apple", "orange", "banana"}
if "banana" in fruits:
  print("있음")
else:
  print("없음")

# 공통 요소 찾기 (교집합)
# 아래 두 집합에서 공통으로 존재하는 요소만 출력하세요.
a = {"apple", "banana", "cherry"}
b = {"banana", "kiwi", "apple"}
print(a & b)

# 차집합 구하기
# 아래 집합 a에서 집합 b에 없는 요소만 출력하세요.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a-b)

# 문자열에서 모음만 set으로 만들기
# 주어진 문자열에서 모음만 골라 set으로 만들고 출력하세요.
text = "I love Python programming"
# 모음: a, e, i, o, u
aa = ["a", "e", "i", "o", "u"]
set_a = set()
cc = text.replace(" ", "").lower()
for i in text:
  if i in aa:
    set_a.add(i)
print(set_a)