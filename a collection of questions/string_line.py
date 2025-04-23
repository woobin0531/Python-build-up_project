# 문자열 길이 구하기
# 아래 문자열의 길이를 구하세요.
text = "Hello, Python!"
print(len(text))

# 문자열 뒤집기
# 아래 문자열을 뒤집어서 출력하세요.
text = "abcdef"
# 출력: "fedcba"
print(text[::-1])

# 공백 기준으로 나누기
# 아래 문자열을 공백 기준으로 나누어 리스트로 출력하세요.
sentence = "Python is very fun"
# 출력: ['Python', 'is', 'very', 'fun']
sentence.split(" ")

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

# 특정 단어 개수 세기
# 아래 문장에서 "Python"이 몇 번 나오는지 세어 출력하세요 (대소문자 구분 없이).
sentence = "Python is fun. I love python. PYTHON is powerful."
# 출력 예시: 3
a = sentence.lower().replace(".", "")
print(a.count("python"))

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

# 압축 문자열 만들기
# 문제 설명:연속된 문자가 반복되면 문자와 반복 횟수로 압축하세요.
# 예: "aaabccccdd" → "a3b1c4d2"
text = "aaabccccdd"
압축 = ""
count = 1

for i in range(1, len(text)):
  if text[i] == text[i - 1]:
    count += 1
  else:
    압축 += text[i - 1] + str(count)
    count = 1
압축 += text[-1] + str(count)
print(압축)

# 가장 많이 등장한 문자 찾기
#문제 설명:문자열에서 가장 많이 등장한 알파벳을 출력하세요.
#공백, 특수기호 제외하고 대소문자 구분 없이 계산하세요.
text = "This is a sample sentence for testing."
text = text.lower()

# 알파벳만 필터링
text = [ch for ch in text if ch.isalpha()]

# 가장 많이 등장한 문자 찾기
max_count = 0
max_char = ""
for ch in text:
    count = text.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print(f"가장 많이 등장한 문자: {max_char} (횟수: {max_count})")

# 특정 패턴 제거하기
#문제 설명: 문자열에서 아래 조건을 만족하는 단어들을 모두 제거한 새 문자열을 출력하세요.
#제거 조건:모두 대문자인 단어, 숫자가 포함된 단어, 길이가 1인 단어
text = "I LOVE Python3 and AI in 2025!"

words = text.split()
result = []

for word in words:
    if word.isupper():
        continue
    elif any(char.isdigit() for char in word):
        continue
    elif len(word) == 1:
        continue
    else:
        result.append(word)

final_text = ' '.join(result)
print(final_text)

# 문자열 길이 출력하기
# 주어진 문자열의 길이를 출력하세요.
text = "Hello, world!"
# 출력 예시: 13
print(len(text))

# 문자열 길이 출력하기
# 주어진 문자열의 길이를 출력하세요.
text = "Hello, world!"
# 출력 예시: 13
print(len(text))

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

# 단어 개수 세기
sentence = "Life is too short to be sad"
words = sentence.split()
count = 0
for _ in words:
    count += 1
print(count)  # 7

# 중복 문자 제거 (순서 유지)
# 설명: 문자열에서 중복된 문자를 제거하되, 처음 등장한 순서를 유지하세요.
# 예시: "banana" → "ban"
def remove_t(n):
  n_remove = ""
  for i in n:
    if i not in n_remove:
      n_remove += i
  return n_remove
remove_t("banana")

# 문자열 압축 (연속된 문자 개수)
# 설명: 연속해서 나오는 문자를 문자 + 개수 형태로 압축하세요.
# 예시: "aaabbccccd" → "a3b2c4d1"
def compress(s):
  result = ""
  count = 1
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      count += 1
    else:
      result += s[i-1] + str(count)
      count = 1
  result += s[-1] + str(count)
  print(result)
compress("aaabbccccd")

# 가장 긴 단어 찾기
# 설명: 문장에서 가장 긴 단어를 출력하세요. 문장 부호는 무시합니다.
# 예시: "Life is short, you need Python and coffee." → "Python"
a = "Life is short, you need Python and coffee."
b = a.replace(',', '').replace('.', '').split(" ")
long_char = ""
for word in b:
  if len(word) > len(long_char):
    long_char = word
print(long_char)
