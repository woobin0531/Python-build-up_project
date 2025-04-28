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

7
# 특정 단어 포함 여부 확인
# 주어진 문자열에 "Python" 이라는 단어가 포함되어 있는지 확인하고,
# 포함되어 있으면 "포함됨", 아니면 "포함되지 않음"을 출력하세요.
a = "I love Python"
b = "Python"
if i in b:
  print("포함됨")
else:
  print("포함안됨")

8
# 문자열에서 첫 번째와 마지막 글자 추출
# 주어진 문자열에서 첫 번째 글자와 마지막 글자를 출력하세요.
# 예시: "Python" → 첫 글자: P, 마지막 글자: n
a = "Python"
print(f"첫글자:{a[0]}, 마지막글자: {a[-1]}")

9
# 문자열에서 특정 문자 위치 찾기
# 주어진 문자열에서 **첫 번째 'o'**가 등장하는 인덱스를 찾으세요.
# 만약 없다면 "문자 없음"을 출력하세요.
a = "Python"
print(a.find("o"))

10
# 문자열에서 단어의 개수 세기
# 주어진 문자열에서 단어의 개수를 출력하세요. 단어는 공백을 기준으로 구분됩니다
a = "I love Python"
b = a.split(" ")
print(len(b))