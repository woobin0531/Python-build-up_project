1
# 두 집합의 공통 접미사 찾기
# 문제 설명:두 리스트에 있는 문자열 중, 뒤에서 3글자가 같은 항목만 뽑아 set으로 출력하세요.
words1 = ["information", "caution", "station", "cat", "elevation"]
words2 = ["vacation", "relation", "bat", "foundation", "nation"]
common_suffix = set()
for w1 in words1:
  for w2 in words2:
    if w1[-3:] == w2[-3:]:
      common_suffix.add(w1)
      common_suffix.add(w2)
print(common_suffix)

2
# 알파벳 포함 여부 확인
# 문장에서 사용된 알파벳만 집합으로 추출하고, a~z까지 모든 알파벳이 포함되었는지 확인하세요.
sentence = "The quick brown fox jumps over the lazy dog"
# 출력 예시: True  (영문 알파벳 26개가 전부 포함되어 있음)
a = set(char.lower() for char in sentence if char.isalpha())
b = set("abcdefghijklmnopqrstuvwxyz")
print(a == b)

3
# 중복 없이 두 리스트의 모든 숫자 합치기
# 두 개의 리스트가 주어졌을 때, 중복 없이 모든 숫자를 합쳐서 정렬된 리스트로 반환하세요.
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
c = []
for i in a+b:
  if i not in c:
    c.append(i)
c.sort()
print(c)

4
# 공통 단어 길이의 평균 구하기
# 두 문장에서 공통으로 등장하는 단어들의 길이 평균을 구하세요. (소문자로 비교)
sentence1 = "Python is a great programming language"
sentence2 = "Learning python language is fun"

s1 = sentence1.lower().split()
s2 = sentence2.lower().split()

a = []
for word in s1:
    if word in s2 and word not in a:
        a.append(word)

if len(a) != 0:
    total_a = 0
    for word in a:
        total_a += len(word)
    avr = total_a / len(a)
else:
    avr = 0
print(avr)
