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

# 튜플에서 합계 구하기
# 주어진 튜플의 모든 숫자를 더한 값을 출력하세요.
numbers = (1, 2, 3, 4, 5)
# 출력 예시: 15
print(sum(numbers))

# 특정 값 개수 세기
# 주어진 튜플에서 숫자 2가 몇 번 나오는지 세어 출력하세요.
numbers = (1, 2, 3, 2, 4, 2, 5)
# 출력 예시: 3
numbers.count(2)

# 튜플을 문자열로 바꾸기
# 문자열로 이루어진 튜플이 주어졌을 때, 공백을 구분자로 한 문자열로 바꾸세요.
words = ('Hello', 'world', 'Python')
# 출력 예시: "Hello world Python"
for i in words:
  print(i, end=" ")

# 튜플에서 짝수만 골라 출력하기
# 설명: 주어진 튜플에서 짝수만 골라 리스트로 출력하세요.
numbers = (10, 15, 22, 33, 40, 55)
# 출력 예시: [10, 22, 40]
t_num = []
for i in numbers:
  if i % 2 == 0:
    t_num.append(i)
print(t_num)

# 튜플에서 특정 값의 개수 세기
# 설명: 주어진 튜플에서 숫자 7이 몇 번 등장하는지 세어 출력하세요.
nums = (7, 3, 5, 7, 8, 7, 2)
# 출력 예시: 3
nums.count(7)

# 중첩 튜플에서 모든 값의 합 구하기
# 설명: 중첩된 튜플 구조에서 모든 숫자의 합을 구해 출력하세요.
data = ((1, 2), (3, 4), (5,))
# 출력 예시: 15
data1 = []
for i in data:
  for ii in i:
    data1.append(ii)
print(sum(data1))

# 교집합 구하기
# 설명: 아래 두 튜플에서 공통으로 들어 있는 요소만 골라 리스트로 출력하세요.
a = (1, 2, 3, 4, 5)
b = (4, 5, 6, 7, 8)
# 출력 예시: [4, 5]
aa = []
for i in a:
  if i in b:
    aa.append(i)
print(aa)

# 튜플 압축하기
# 두 튜플을 인덱스별로 묶어 리스트 형태로 출력하세요.
names = ("Tom", "Jerry", "Spike")
scores = (85, 90, 88)
# 출력 예시: [('Tom', 85), ('Jerry', 90), ('Spike', 88)]
t = []
for i in range(len(names)):
  t.append((names[i], scores[i]))
print(t)

# 튜플에서 최댓값과 최솟값 찾기
# 주어진 튜플에서 최대값과 최소값을 각각 출력하세요.
nums = (11, 4, 99, 23, 7)
# 출력 예시:
# 최대값: 99
# 최소값: 4
print(f"최대값은 {max(nums)}, 최소값은{min(nums)}입니다.")
"""
nums = (11, 4, 99, 23, 7)
max_num = nums[0] min_num = nums[0]
for i in nums: if i > max_num: max_num = i if i < min_num: min_num = i
print("최대값:", max_num) print("최소값:", min_num)
"""

