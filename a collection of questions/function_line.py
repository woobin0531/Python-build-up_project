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
