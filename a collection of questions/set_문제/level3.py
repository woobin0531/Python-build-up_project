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

5
# 여러 집합의 연산과 집합 메서드 활용
# 아래 세 집합이 있습니다.
# 세 집합의 모든 원소가 한 번씩만 포함된 집합(합집합)을 구하세요.
# 세 집합 모두에 공통으로 들어 있는 원소(교집합)를 구하세요.
# set_a에만 있고 set_b, set_c에는 없는 원소의 집합(차집합)을 구하세요.
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7}

print(set_a | set_b | set_c)
print(set_a & set_b & set_c)
print(set_a - (set_b | set_c))

6
# 집합을 이용한 아나그램 판별 함수 만들기
# 두 개의 단어가 주어졌을 때,
# 각 단어에 사용된 알파벳 종류가 정확히 같으면 True,
# 아니면 False를 반환하는 함수를 작성하세요.
# (단, 대소문자는 구분하지 않고, 알파벳 이외의 문자는 무시합니다.)
# 예시1
word1 = "Listen!"
word2 = "Silent"
# → True
# 예시2
word1 = "Python"
word2 = "Typhon"
# → True

import string

def a_set(word1, word2):
  w1 = set(i.lower() for i in word1 if i.isalpha())
  w2 = set(i.lower() for i in word2 if i.isalpha())
  return w1 == w2

print(a_set("Listen!", "Silent"))

7
# 집합을 활용한 데이터 중복 제거 및 정렬
# 아래와 같이 여러 번 등장하는 숫자가 있는 리스트가 있습니다.
# 이 리스트에서 중복을 제거하고,
# 남은 숫자들을 오름차순으로 정렬한 리스트로 만드세요.
nums = [5, 3, 8, 3, 1, 5, 9, 1, 2]
sorted_num = sorted(set(nums))
print(sorted_num)