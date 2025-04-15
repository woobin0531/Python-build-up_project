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