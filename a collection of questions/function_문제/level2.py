1
# 짝수만 골라서 반환하기
# 주어진 리스트에서 짝수만 골라서 새로운 리스트로 반환하는 함수를 작성하세요
def even_only(x):
  answer = []
  for i in x:
    if i % 2 == 0:
      answer.append(i)
  return answer

print(even_only([1, 2, 3, 4, 5, 6]))

2
# 문자열 길이 반환하기
# 여러 문자열이 담긴 리스트를 받아 각각의 문자열 길이만 모아 새로운 리스트로 반환하는 함수를 작성하세요.
def string_lengths(x):
  answer = []
  for i in x:
    answer.append(len(i))
  return answer
print(string_lengths(["hello", "hi", "python"]))

3
# 특정 글자 세기
# 문자열과 특정 문자를 받아, 문자열 안에 해당 문자가 몇 번 등장하는지 반환하는 함수를 작성하세요
def count_char(x, y):
    return x.count(y)
print(count_char("banana", "a"))

4
# 양수/음수/0 판별 함수
# 정수를 입력받아 양수면 "positive", 음수면 "negative", 0이면 "zero"를 반환하는 함수를 작성하세요.
def check_sign(a):
  a = int(input())
  if a > 0:
    print("positive")
  elif a == 0:
    print("zero")
  else:
    print("negative")
  return a
check_sign(2)
"""
def check_sign(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(check_sign(-5))  # 출력: "negative"
print(check_sign(0))   # 출력: "zero"
print(check_sign(7))   # 출력: "positive"
"""

5
# 두 리스트의 교집합 구하기
# 두 리스트가 주어졌을 때, 공통된 항목만 뽑아 리스트로 반환하는 함수를 작성하세요.
#예시:
#입력: [1, 2, 3, 4], [3, 4, 5, 6]
#출력: [3, 4]
def same_thing(a, b):
  result = []
  for item in a:
    if item in b and item not in result:
      result.append(item)
  return result
print(same_thing([1, 2, 3, 4], [3, 4, 5, 6]))

6
# 특정 글자 개수 세기
# 문자열과 특정 문자를 입력 받아, 해당 문자가 문자열에 몇 번 등장하는지 반환하는 함수를 작성하세요.
#예시:
#입력: "banana", 'a'
#출력: 3
def count_char(text, target):
  count = 0
  for char in text:
    if char == target:
      count += 1
  return count
print(count_char("banana", "a"))

7
# 리스트에서 짝수만 추출
# 정수 리스트를 입력받아, 짝수만 모은 새 리스트를 반환하는 함수를 작성하세요.
# 함수 이름: get_even_numbers
# 입력: 정수 리스트
# 반환: 짝수만 담긴 리스트
def get_even_numbers(a):
  return [num for num in a if num % 2 == 0]
print(get_even_numbers([1, 2, 3, 4, 5]))

8
# 단어 개수 세기
# 문자열 하나를 입력받아, 그 안에 있는 단어(word) 의 개수를 반환하는 함수를 작성하세요.
# (단어는 띄어쓰기로 구분합니다.)
# 함수 이름: count_words
# 입력: 문자열 1개
# 반환: 단어 개수 (정수)
def count_words(s):
  a =s.split(" ")
  return len(a)
print(count_words("I love Python") )

9
# 중복 제거 후 정렬
# 리스트를 입력받아, 중복을 제거하고 오름차순으로 정렬한 새 리스트를 반환하는 함수를 작성하세요.
# 함수 이름: remove_duplicates_and_sort
# 입력: 리스트 (숫자 또는 문자열)
# 반환: 중복 없이 정렬된 리스트
def remove_duplicates_and_sort(a):
  b = sorted(set(a))
  c = list(b)
  return c
print(remove_duplicates_and_sort([1, 2, 3, 3, 4]))

10
# 리스트를 문자열로 변환
# 문자열 리스트를 입력받아, 콤마(,)로 연결된 하나의 문자열로 반환하는 함수를 작성하세요.
# 함수 이름: list_to_string
# 입력: 문자열 리스트
# 반환: 하나의 문자열
def list_to_string(a):
  b = ",".join(a)
  return b
print(list_to_string(["a", "b", "c"]))

11
# 주어진 리스트에서 특정 숫자가 몇 번 등장하는지 세는 함수를 작성하세요.
# 함수를 사용하여 주어진 리스트에서 특정 숫자의 등장 횟수를 출력해 보세요.
# my_list = [1, 2, 3, 4, 2, 1, 5, 2, 6]
# target_number = 2
def count_number(my_list, target_number):
  count = 0
  for num in my_list:
    if num == target_number:
      count += 1
  print(f"{target_number}숫자는 {count}번 입니다.")

my_list = [1, 2, 3, 4, 2, 1, 5, 2, 6]
target_number = 2
count_number(my_list, target_number)

12
# 최댓값과 최솟값을 동시에 반환하는 함수
# 숫자 리스트를 받아서, 최댓값과 최솟값을 튜플로 반환하는 함수를 작성하세요.
# 조건
# 입력: 숫자 리스트
# 반환: (최댓값, 최솟값) 형태의 튜플
def find_max_min(a):
  b = max(a)
  c = min(a)
  return (b, c)

print(find_max_min([2, 3, 4, 5, 6]))