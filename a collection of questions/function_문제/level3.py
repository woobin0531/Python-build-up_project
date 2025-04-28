1
# 단어 길이 기준 정렬하기
#주어진 단어 리스트를 단어 길이 기준으로 오름차순 정렬하여 반환하는 함수를 작성하세요.
#단, 길이가 같으면 사전 순으로 정렬합니다.
def sorted_words(words):
  return sorted(words, key= lambda x: (len(x), x)) #key = lambda x: (첫번째 기준, 두번째 기준)

words = ["banana", "apple", "kiwi", "grape", "pear", "peach"]
print(sorted_words(words))

2
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

3
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

4
# 단어 길이 기준 정렬
#문제 설명:
#단어 리스트를 받아서, 단어의 길이 기준으로 정렬하되, 길이가 같으면 사전 순으로 정렬하여 반환하는 함수를 작성하세요.
#예:
# ["banana", "apple", "kiwi", "grape", "pear", "peach"]
# → ['kiwi', 'pear', 'apple', 'grape', 'peach', 'banana']
def sorted_list(a):
    return sorted(a, key=lambda x: (len(x), x))

sorted_list(["banana", "apple", "kiwi", "grape", "pear", "peach"])

5
# 팩토리얼 계산
# 양의 정수 하나를 입력받아, 그 수의 팩토리얼을 반환하는 함수를 작성하세요.
# (팩토리얼: n! = n × (n-1) × (n-2) × ... × 1)
# 함수 이름: factorial
# 입력: 양의 정수 1개
# 반환: 팩토리얼 값 (정수)
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
print(factorial(5))