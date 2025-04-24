# 숫자 두 개 더하기
# 문제: 두 개의 정수를 입력받아 그 합을 반환하는 함수를 작성하세요.
def add_numbers(x, y):
  return x + y
print(add_numbers(3, 5))

# 리스트 평균 구하기
# 문제: 숫자로 이루어진 리스트를 받아 평균을 반환하는 함수를 작성하세요.
def average(x):
  return sum(x)/len(x)
print(average([10, 20, 30]))

# 문자열 거꾸로 출력하기
# 주어진 문자열을 거꾸로 뒤집어 반환하는 함수를 작성하세요.
def reverse_string(x):
  return x[::-1]
print(reverse_string("hello"))

# 짝수만 골라서 반환하기
# 주어진 리스트에서 짝수만 골라서 새로운 리스트로 반환하는 함수를 작성하세요
def even_only(x):
  answer = []
  for i in x:
    if i % 2 == 0:
      answer.append(i)
  return answer

print(even_only([1, 2, 3, 4, 5, 6]))

# 문자열 길이 반환하기
# 여러 문자열이 담긴 리스트를 받아 각각의 문자열 길이만 모아 새로운 리스트로 반환하는 함수를 작성하세요.
def string_lengths(x):
  answer = []
  for i in x:
    answer.append(len(i))
  return answer
print(string_lengths(["hello", "hi", "python"]))

# 특정 글자 세기
# 문자열과 특정 문자를 받아, 문자열 안에 해당 문자가 몇 번 등장하는지 반환하는 함수를 작성하세요
def count_char(x, y):
    return x.count(y)
print(count_char("banana", "a"))

# 단어 길이 기준 정렬하기
#주어진 단어 리스트를 단어 길이 기준으로 오름차순 정렬하여 반환하는 함수를 작성하세요.
#단, 길이가 같으면 사전 순으로 정렬합니다.
def sorted_words(words):
  return sorted(words, key= lambda x: (len(x), x)) #key = lambda x: (첫번째 기준, 두번째 기준)

words = ["banana", "apple", "kiwi", "grape", "pear", "peach"]
print(sorted_words(words))

# 숫자를 영어로 바꾸기
# 정수를 입력받아 0~9 숫자를 영어로 바꾼 문자열을 반환하는 함수를 작성하세요.
def number_to_english(n):
    digit_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    result = []
    for digit in str(n):
        result.append(digit_words[int(digit)])
    return " ".join(result)

# 사용자에게 정수 입력 받기
user_input = int(input("정수를 입력하세요: "))
print(number_to_english(user_input))

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
