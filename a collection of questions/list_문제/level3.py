1
# 리스트를 반으로 나누기
# 아래 리스트를 반으로 나눠서 두 개의 리스트로 출력하세요. (요소 개수가 홀수면 앞쪽이 하나 더 많아야 함)
numbers = [10, 20, 30, 40, 50, 60, 70]
# 예: [10, 20, 30, 40], [50, 60, 70]
mid = (len(numbers) + 1)// 2
a = numbers[:mid]
b = numbers[mid:]
print(a)
print(b)

2
# 중첩 리스트의 총합 구하기
# 아래 2차원 리스트의 모든 숫자들의 합을 구해 출력하세요.
matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
matrix_a = 0
for i in matrix:
 matrix_a += sum(i)
print(matrix_a)

3
# 중복 제거 후 정렬하기
# 리스트에 중복된 값을 제거하고, 오름차순으로 정렬한 리스트를 출력하세요.
nums = [4, 1, 7, 2, 4, 7, 5, 2, 9]
# 출력 예시: [1, 2, 4, 5, 7, 9]
sorted_nums = []
for i in nums:
  if i not in sorted_nums:
    sorted_nums.append(i)
print(sorted(sorted_nums))

4
# 숫자 리스트를 문자열로 연결하기
# 숫자로 이루어진 리스트를 문자열로 연결하세요.
nums = [1, 2, 3, 4]
# 출력 예시: "1234"
new = ""
for i in nums:
  new += str(i)
print(new)

5
# 가장 많이 등장한 숫자 구하기
# 리스트에서 가장 자주 등장한 숫자를 출력하세요.
nums = [1, 2, 2, 3, 3, 3, 4, 4]
# 출력 예시: 3
num = None
max_count = 0

for i in nums:
  count = nums.count(i)
  if count > max_count:
    max_count = count
    num = i
print(num)