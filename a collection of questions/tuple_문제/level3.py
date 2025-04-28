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