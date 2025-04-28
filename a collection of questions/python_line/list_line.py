# 리스트의 길이 출력하기
# 아래 리스트에 들어있는 요소의 개수를 출력하세요.
colors = ["red", "blue", "green", "yellow", "pink"]
print(len(colors))

# 리스트의 마지막 요소 출력하기
# 아래 리스트의 마지막 값을 출력하세요.
numbers = [11, 22, 33, 44, 55]
print(numbers[-1])

# 문자열 리스트에서 첫 글자만 모으기
# 아래 문자열 리스트에서 각 단어의 첫 글자만 모아 새로운 리스트로 만들어 출력하세요.
words = ["apple", "banana", "cherry", "date"]
# 결과 예시: ['a', 'b', 'c', 'd']
word = []
for i in words:
  word.append(i[0])
print(word)
#############################
# 양수만 추출하기
# 아래 리스트에서 0보다 큰 숫자만 골라 새로운 리스트에 담아 출력하세요.
numbers = [3, -1, 0, 7, -5, 9, -2]
z_numbers = []
for i in numbers:
  if i > 0:
    z_numbers.append(i)
print(z_numbers)

# 리스트 요소들의 평균 구하기
# 아래 리스트에 들어있는 숫자들의 평균(총합 ÷ 개수)을 출력하세요.
scores = [70, 85, 90, 100, 65]
avr = sum(scores)/len(scores)
print(avr)

# 중복 제거한 리스트 만들기
# 아래 리스트에서 중복을 제거하고, 순서를 유지한 새로운 리스트를 만들어 출력하세요.
items = [1, 3, 3, 5, 1, 7, 9, 5, 9]
# 결과 예시: [1, 3, 5, 7, 9]
a = []
for item in items:
  if item not in a:
    a.append(item)
print(a)

# 리스트를 반으로 나누기
# 아래 리스트를 반으로 나눠서 두 개의 리스트로 출력하세요. (요소 개수가 홀수면 앞쪽이 하나 더 많아야 함)
numbers = [10, 20, 30, 40, 50, 60, 70]
# 예: [10, 20, 30, 40], [50, 60, 70]
mid = (len(numbers) + 1)// 2
a = numbers[:mid]
b = numbers[mid:]
print(a)
print(b)

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

# 가장 많이 등장한 값 찾기
# 아래 리스트에서 가장 많이 등장한 숫자를 찾아 출력하세요.
nums = [1, 3, 1, 7, 3, 1, 3, 3, 9, 1, 1]
# (최빈값을 구하는 문제)
max_count = 0
most_common = None
for i in nums:
  count = nums.count(i)
  if count > max_count:
    max_count = count
    most_common = i
print(most_common)

# 특정 값 세기
# 주어진 리스트에서 숫자 3이 몇 번 나오는지 출력하세요.
numbers = [1, 3, 5, 3, 7, 3, 9]
# 출력 예시: 3
print(numbers.count(3))

# 리스트 뒤집기
# 주어진 리스트를 뒤집어서 출력하세요.
fruits = ["apple", "banana", "cherry"]
# 출력 예시: ['cherry', 'banana', 'apple']
print(fruits[::-1])

# 모든 요소 더하기
# 아래 리스트에 있는 모든 숫자의 합을 구하세요.
scores = [85, 90, 78, 92, 88]
# 출력 예시: 433
print(sum(scores))

# 짝수만 골라 리스트 만들기
# 주어진 리스트에서 짝수만 골라 새로운 리스트를 만드세요.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 출력 예시: [2, 4, 6, 8, 10]
t_numbers = []
for t in numbers:
  if t % 2 == 0:
    t_numbers.append(t)
print(t_numbers)

# 가장 긴 문자열 찾기
# 아래 리스트에서 가장 길이가 긴 문자열을 출력하세요.
words = ["dog", "elephant", "cat", "hippopotamus", "lion"]
# 출력 예시: "hippopotamus"
most_list = []
for i in words:
  if len(i) > len(most_list):
    most_list = i
print(most_list)

# 두 리스트의 교집합 구하기
# 두 리스트에 공통으로 들어있는 숫자만 골라 새로운 리스트로 만드세요.
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
# 출력 예시: [4, 5]
c = []
for i in a:
  if i in b:
    c.append(i)
print(c)

# 중복 제거 후 정렬하기
# 리스트에 중복된 값을 제거하고, 오름차순으로 정렬한 리스트를 출력하세요.
nums = [4, 1, 7, 2, 4, 7, 5, 2, 9]
# 출력 예시: [1, 2, 4, 5, 7, 9]
sorted_nums = []
for i in nums:
  if i not in sorted_nums:
    sorted_nums.append(i)
print(sorted(sorted_nums))

# 숫자 리스트를 문자열로 연결하기
# 숫자로 이루어진 리스트를 문자열로 연결하세요.
nums = [1, 2, 3, 4]
# 출력 예시: "1234"
new = ""
for i in nums:
  new += str(i)
print(new)

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