1
# 튜플 압축하기
# 아래와 같은 두 튜플이 있을 때, 인덱스별로 묶어서 하나의 튜플 리스트로 만들어보세요.
names = ("Alice", "Bob", "Charlie")
scores = (90, 85, 92)
a = []
for i in range(len(names)):
  a.append((names[i], scores[i]))
print(a)

2
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

3
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

4
# 튜플 압축하기
# 두 튜플을 인덱스별로 묶어 리스트 형태로 출력하세요.
names = ("Tom", "Jerry", "Spike")
scores = (85, 90, 88)
# 출력 예시: [('Tom', 85), ('Jerry', 90), ('Spike', 88)]
t = []
for i in range(len(names)):
  t.append((names[i], scores[i]))
print(t)

5
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

6
# 튜플 불변성 우회 및 값 변경
# 튜플은 불변(immutable) 자료형이기 때문에 요소를 직접 변경할 수 없습니다.
# 아래 튜플에서 두 번째 값을 99로 바꾼 새로운 튜플을 만드는 코드를 작성하세요.
t = (10, 20, 30, 40)
new_t = t[:1] + (99,) + t[2:]
print(new_t)

7
# 튜플 언패킹과 함수 반환값 활용
# 두 개의 정수를 입력받아, 그 합, 차, 곱, 몫, 나머지를 튜플로 반환하는 함수를 작성하고,
# 반환된 튜플을 언패킹하여 각각의 값을 출력하세요
def calc(a, b):
  return (a + b, a - b, a * b, a // b, a % b)

result = calc(20, 7)
_sum, diff, prod, quot, remain = result

print("합:", _sum)      # 27
print("차:", diff)      # 13
print("곱:", prod)      # 140
print("몫:", quot)      # 2
print("나머지:", remain) # 6

8
# 튜플 컴프리헨션(표현식) 활용
# 1부터 20까지의 수 중에서 3의 배수만을 포함하는 튜플을 한 줄의 코드로 생성하세요.
result = tuple(x for x in range(1, 21) if x % 3 == 0)
print(result)
