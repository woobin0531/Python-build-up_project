# 튜플에서 홀수만 추출하기
numbers = (1, 2, 3, 4, 5, 6, 7)
# 출력 예시: (1, 3, 5, 7)
print(numbers[0::2])

# 튜플의 최대값과 최소값 출력하기
data = (10, 25, 7, 50, 34)
# 출력 예시: max: 50, min: 7
a = max(data)
b = min(data)
print("max:",a ,"min:", b)

# 튜플에서 문자열의 길이 출력하기
words = ("apple", "banana", "kiwi")
# 출력 예시: 5 6 4
for i in words:
  print(len(i), end=" ")

# 튜플 요소 뒤집기
# 문제 설명: 아래 튜플의 각 문자열을 뒤집어서 새로운 튜플로 만들어 출력하세요.
words = ("apple", "banana", "grape")
# 출력 예시: ('elppa', 'ananab', 'eparg')
re_words = tuple(word[::-1] for word in words)
print(re_words)

# 평균이 80 이상인 학생 이름 출력
students = (
    ("Anna", (85, 92, 78)),
    ("Ben", (70, 68, 75)),
    ("Clara", (90, 88, 95))
)
# 출력 예시: Anna Clara
for name, scores in students:
  avg = sum(scores) / len(scores)
  if avg >= 80:
    print(name)

# 두 튜플의 교집합 구하기
# 아래 두 튜플에서 겹치는 값을 set으로 출력하세요.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7)
# 출력 예시: {4, 5}
a = set(t1)
b = set(t2)
print(a&b)

# 튜플 압축하기
# 아래와 같은 두 튜플이 있을 때, 인덱스별로 묶어서 하나의 튜플 리스트로 만들어보세요.
names = ("Alice", "Bob", "Charlie")
scores = (90, 85, 92)
a = []
for i in range(len(names)):
  a.append((names[i], scores[i]))
print(a)

# 중첩 튜플에서 최대값 찾기
# 아래 중첩된 튜플 구조에서 가장 큰 숫자를 찾아 출력하세요.
numbers = ((1, 5, 9), (3, 7), (8, 2, 10, 4))
# 출력예시: 10
max_number = -1
for group in numbers:
  group_max = max(group)
  if group_max > max_number:
    max_number = group_max
print(max_number)