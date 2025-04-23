# 세 수의 평균 구하기
# 세 개의 숫자를 입력받아 평균을 반환하는 함수를 작성하세요.
def average(x, y, z):
  a = [x, y, z]
  b =sum(a) / len(a)
  return b
average(3, 7, 10)
"""
def average(a, b, c):
    return (a + b + c) / 3
print(average(3, 7, 10))  # 출력: 6.666666666666667
"""

# 문자열을 거꾸로 반환하기
# 문자열을 받아 거꾸로 뒤집어 반환하는 함수를 작성하세요.
def reverse_string(x):
  return x[::-1]
reverse_string("hello")

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

# 문자열에서 대문자만 추출하기
# 주어진 문자열에서 대문자만 추출하여 새로운 문자열로 반환하는 함수를 작성하세요.
#예시:
#입력: "Hello World!"
#출력: "HW"
def string_upper(a):
  answer =  ""
  for i in a:
    if i.isupper():
      answer += i
  return answer
print(string_upper("Hello World"))

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

# 문자열 압축하기
# 문제 설명:
# 연속된 문자가 반복되면 문자와 반복 횟수로 압축한 문자열을 반환하는 함수를 작성하세요.
# 예: "aaabccccdd" → "a3b1c4d2"
def hurrykane(s):
  if not s:
    return ""

  result = ""
  count = 1
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      count += 1
    else:
      result += s[i-1] + str(count)
      count = 1
  result += s[-1] + str(count)
  return result

print(hurrykane("aabbcccdddd"))

# 단어 길이 기준 정렬
#문제 설명:
#단어 리스트를 받아서, 단어의 길이 기준으로 정렬하되, 길이가 같으면 사전 순으로 정렬하여 반환하는 함수를 작성하세요.
#예:
# ["banana", "apple", "kiwi", "grape", "pear", "peach"]
# → ['kiwi', 'pear', 'apple', 'grape', 'peach', 'banana']
def sorted_list(a):
    return sorted(a, key=lambda x: (len(x), x))

sorted_list(["banana", "apple", "kiwi", "grape", "pear", "peach"])