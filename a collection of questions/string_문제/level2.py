1
# 대소문자 수 세기
# 아래 문자열에서 대문자와 소문자의 개수를 각각 구하세요.
text = "Hello World! Python is AMAZING."
# 출력 예시: 대문자 4개, 소문자 21개
count_upper = 0
count_lower = 0
a = text.replace("!", "").replace(".", "")
for i in a:
  if i.isupper():
    count_upper += 1
  if i.islower():
    count_lower += 1
print(count_upper, count_lower)

2
# 특정 단어 개수 세기
# 아래 문장에서 "Python"이 몇 번 나오는지 세어 출력하세요 (대소문자 구분 없이).
sentence = "Python is fun. I love python. PYTHON is powerful."
# 출력 예시: 3
a = sentence.lower().replace(".", "")
print(a.count("python"))

3
#가장 긴 단어 찾기
# 아래 문장에서 가장 긴 단어를 출력하세요.
sentence = "Life is short, you need Python and coffee."
# 문장 내 쉼표와 마침표 제거
cleaned_sentence = sentence.replace(",", "").replace(".", "")
# 단어로 나누기
words = cleaned_sentence.split()
# 가장 긴 단어 찾기
king_word = ""
for i in words:
    if len(i) > len(king_word):
        king_word = i
print(king_word)


4
# 대소문자 변환
# 문제: 주어진 문자열에서 소문자는 대문자로, 대문자는 소문자로 바꾸시오
a = "Hello World"
b = ""
for i in a:
  if i.islower():
    b += i.upper()
  elif i.isupper():
    b += i.lower()
  else:
    b += i
print(b)

5
# 문자 제거하기
# 문제: 주어진 문자열에서 특정 문자를 모두 제거하세요
# 문자열 "banana" 와 문자 "a"
# 출력: "bnn"
text = "banana"
remove = "a"
result = ""
for i in text:
  if i != remove:
    result += i
print(result)

6
# 단어 개수 세기
sentence = "Life is too short to be sad"
words = sentence.split()
count = 0
for _ in words:
    count += 1
print(count)  # 7