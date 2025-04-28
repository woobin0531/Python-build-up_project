1
# 숫자 두 개 더하기
# 문제: 두 개의 정수를 입력받아 그 합을 반환하는 함수를 작성하세요.
def add_numbers(x, y):
  return x + y
print(add_numbers(3, 5))

2
# 리스트 평균 구하기
# 문제: 숫자로 이루어진 리스트를 받아 평균을 반환하는 함수를 작성하세요.
def average(x):
  return sum(x)/len(x)
print(average([10, 20, 30]))

3
# 문자열 거꾸로 출력하기
# 주어진 문자열을 거꾸로 뒤집어 반환하는 함수를 작성하세요.
def reverse_string(x):
  return x[::-1]
print(reverse_string("hello"))

4
# 사용자에게 정수 입력 받기
user_input = int(input("정수를 입력하세요: "))
print(number_to_english(user_input))

5
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

6
# 문자열을 거꾸로 반환하기
# 문자열을 받아 거꾸로 뒤집어 반환하는 함수를 작성하세요.
def reverse_string(x):
  return x[::-1]
reverse_string("hello")

7
# 문제: 세 수 중 가장 큰 수 찾기
# 정수 3개를 입력받아, 가장 큰 수를 반환하는 함수를 작성하세요.
# 함수 이름: find_max
# 입력: 세 개의 정수
# 반환: 가장 큰 수 (정수)
def find_max(a, b, c):
  return max(a, b, c)

print(find_max(2, 3, 4))

8
# 문자열 길이 구하기
# 문자열 하나를 입력받아, 그 문자열의 길이를 반환하는 함수를 작성하세요.
# 함수 이름: string_length
# 입력: 문자열 1개
# 반환: 문자열의 길이 (정수)
def string_length(a):
  return len(a)

string_length("hello")

9
# 리스트 요소 합계 구하기
# 정수로 이루어진 리스트를 입력받아, 요소들의 합을 반환하는 함수를 작성하세요.
# 함수 이름: list_sum
# 입력: 정수 리스트
# 반환: 합계 (정수)
def list_sum(a):
  return sum(a)
print(list_sum([1, 2, 3, 4]))

10
# 문자열 뒤집기
# 문자열 하나를 입력받아, 거꾸로 뒤집은 문자열을 반환하는 함수를 작성하세요.
# 함수 이름: reverse_string
# 입력: 문자열 1개
# 반환: 뒤집힌 문자열
def reverse_string(a):
  return a[::-1]
print(reverse_string("hello"))