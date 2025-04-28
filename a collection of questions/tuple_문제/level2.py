1
# 튜플 요소 뒤집기
# 문제 설명: 아래 튜플의 각 문자열을 뒤집어서 새로운 튜플로 만들어 출력하세요.
words = ("apple", "banana", "grape")
# 출력 예시: ('elppa', 'ananab', 'eparg')
re_words = tuple(word[::-1] for word in words)
print(re_words)

2
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

3
# 두 튜플의 교집합 구하기
# 아래 두 튜플에서 겹치는 값을 set으로 출력하세요.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7)
# 출력 예시: {4, 5}
a = set(t1)
b = set(t2)
print(a&b)

4
# 튜플을 문자열로 바꾸기
# 문자열로 이루어진 튜플이 주어졌을 때, 공백을 구분자로 한 문자열로 바꾸세요.
words = ('Hello', 'world', 'Python')
# 출력 예시: "Hello world Python"
for i in words:
  print(i, end=" ")

5
# 튜플에서 짝수만 골라 출력하기
# 설명: 주어진 튜플에서 짝수만 골라 리스트로 출력하세요.
numbers = (10, 15, 22, 33, 40, 55)
# 출력 예시: [10, 22, 40]
t_num = []
for i in numbers:
  if i % 2 == 0:
    t_num.append(i)
print(t_num)

6
# 중첩 튜플에서 모든 값의 합 구하기
# 설명: 중첩된 튜플 구조에서 모든 숫자의 합을 구해 출력하세요.
data = ((1, 2), (3, 4), (5,))
# 출력 예시: 15
data1 = []
for i in data:
  for ii in i:
    data1.append(ii)
print(sum(data1))