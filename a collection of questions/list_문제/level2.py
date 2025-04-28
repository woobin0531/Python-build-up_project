1
# 문자열 리스트에서 첫 글자만 모으기
# 아래 문자열 리스트에서 각 단어의 첫 글자만 모아 새로운 리스트로 만들어 출력하세요.
words = ["apple", "banana", "cherry", "date"]
# 결과 예시: ['a', 'b', 'c', 'd']
word = []
for i in words:
  word.append(i[0])
print(word)

2
# 양수만 추출하기
# 아래 리스트에서 0보다 큰 숫자만 골라 새로운 리스트에 담아 출력하세요.
numbers = [3, -1, 0, 7, -5, 9, -2]
z_numbers = []
for i in numbers:
  if i > 0:
    z_numbers.append(i)
print(z_numbers)

3
# 리스트 요소들의 평균 구하기
# 아래 리스트에 들어있는 숫자들의 평균(총합 ÷ 개수)을 출력하세요.
scores = [70, 85, 90, 100, 65]
avr = sum(scores)/len(scores)
print(avr)

4
# 중복 제거한 리스트 만들기
# 아래 리스트에서 중복을 제거하고, 순서를 유지한 새로운 리스트를 만들어 출력하세요.
items = [1, 3, 3, 5, 1, 7, 9, 5, 9]
# 결과 예시: [1, 3, 5, 7, 9]
a = []
for item in items:
  if item not in a:
    a.append(item)
print(a)

5
# 짝수만 골라 리스트 만들기
# 주어진 리스트에서 짝수만 골라 새로운 리스트를 만드세요.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 출력 예시: [2, 4, 6, 8, 10]
t_numbers = []
for t in numbers:
  if t % 2 == 0:
    t_numbers.append(t)
print(t_numbers)

6
# 가장 긴 문자열 찾기
# 아래 리스트에서 가장 길이가 긴 문자열을 출력하세요.
words = ["dog", "elephant", "cat", "hippopotamus", "lion"]
# 출력 예시: "hippopotamus"
most_list = []
for i in words:
  if len(i) > len(most_list):
    most_list = i
print(most_list)

7
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

8
# 중복 제거 후 정렬하기
# 리스트에 중복된 값을 제거하고, 오름차순으로 정렬한 리스트를 출력하세요.
nums = [4, 1, 7, 2, 4, 7, 5, 2, 9]
# 출력 예시: [1, 2, 4, 5, 7, 9]
sorted_nums = []
for i in nums:
  if i not in sorted_nums:
    sorted_nums.append(i)
print(sorted(sorted_nums))

9
# 리스트에 숫자 추가하기
# 빈 리스트를 만들고,
#사용자에게 숫자 3개를 입력받아 리스트에 추가한 후 출력하세요.

num = []
for i in range(3):
  a = int(input("숫자 3개 입력하세요:"))
  num.append(a)
print(num)

10
# 리스트에서 짝수만 추출하기
# 리스트 [1, 2, 3, 4, 5, 6]에서 짝수만 골라 새 리스트로 만들고 출력하세요.
a = [1, 2, 3, 4, 5, 6]
b = [i for i in a if i % 2 == 0]
print(b)

11
# 리스트에서 최댓값과 최솟값 찾기
# 리스트 [12, 45, 2, 19, 78, 34]가 주어졌을 때,
# 최댓값과 최솟값을 찾아 출력하세요.
numbers = [12, 45, 2, 19, 78, 34]
max_num = max(numbers)
min_num = min(numbers)
print(f"최댓값: {max_num}")
print(f"최솟값: {min_num}")

12
# 리스트 요소 뒤집기
# 리스트 [1, 2, 3, 4, 5]를
# 거꾸로 뒤집은 새 리스트를 만들어 출력하세요.
a = [1, 2, 3, 4, 5]
b = a[::-1]
print(b)

13
# 리스트 중 중복 제거 후 오름차순 정렬
# 리스트 [4, 2, 5, 2, 3, 4, 1, 5]가 주어졌을 때,
# 중복을 제거하고 오름차순으로 정렬한 리스트를 출력하세요.
numbers = [4, 2, 5, 2, 3, 4, 1, 5]
# 중복 제거하고 정렬
unique_sorted = sorted(set(numbers))
print(unique_sorted)

14
# 리스트에서 짝수만 골라 새 리스트 만들기
# 리스트 [10, 15, 20, 25, 30, 35, 40]에서
# 짝수만 골라 새로운 리스트를 만들어 출력하세요.
a = [10, 15, 20, 25, 30, 35, 40]
b = [i for i in a if i % 2 == 0]
print(b)

15
# 두 리스트 합치기 (중복 없이)
# 두 리스트를 합쳐서, 중복 없이 하나의 리스트로 만들어 출력하세요.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# 두 리스트 합치고 중복 제거
merged = list(set(list1 + list2))
# 정렬까지 하고 싶으면 추가로
merged_sorted = sorted(merged)
print(merged_sorted)
