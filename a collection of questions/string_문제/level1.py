1
# 문자열 길이 구하기
# 아래 문자열의 길이를 구하세요.
text = "Hello, Python!"
print(len(text))

2
# 문자열 뒤집기
# 아래 문자열을 뒤집어서 출력하세요.
text = "abcdef"
# 출력: "fedcba"
print(text[::-1])

3
# 공백 기준으로 나누기
# 아래 문자열을 공백 기준으로 나누어 리스트로 출력하세요.
sentence = "Python is very fun"
# 출력: ['Python', 'is', 'very', 'fun']
sentence.split(" ")

4
# 문자열 길이 출력하기
# 주어진 문자열의 길이를 출력하세요.
text = "Hello, world!"
# 출력 예시: 13
print(len(text))

5
# 문자열 길이 출력하기
# 주어진 문자열의 길이를 출력하세요.
text = "Hello, world!"
# 출력 예시: 13
print(len(text))

6
# 문자열에 포함된 숫자만 추출하기
# 문자열에서 숫자만 골라서 새로운 문자열로 만들어 출력하세요.
text = "a1b2c3d4"
# 출력 예시: "1234"
c = text[1::2]
print(c)

"""
result = ""
for char in text:
    if char.isdigit():
        result += char
print(result)
"""

7
# 문자열 길이 출력
# 사용자에게 문자열을 입력받아, 그 문자열의 길이를 출력하세요.
a = input("입력하세요: ")
print(len(a))

8
# 문자열 거꾸로 출력
# 사용자에게 문자열을 입력받아,
# 거꾸로 출력하는 프로그램을 작성하세요.
a = input("입력하세요: ")
print(a[::-1])

9
# 문자열에 특정 문자 개수 세기
# 사용자에게 문자열을 입력받고,
# 그 문자열에 'a' 문자가 몇 개 있는지 세어 출력하세요.
a = input("입력하세요: ")
print(a.count("a"))

10
# 문자열에서 대소문자 변환
# 주어진 문자열에서 모든 소문자를 대문자로 변환한 결과를 출력하세요.
a = "python"
b = a.upper()
print(b)

11
# 문자열에서 모든 공백 제거
# 주어진 문자열에서 모든 공백을 제거한 새로운 문자열을 출력하세요.
# 예시: " I love Python " → "IlovePython"
a = " I love Python "
print(a.replace(" ", ""))