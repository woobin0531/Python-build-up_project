# 중복 제거하기
# 리스트에서 중복된 항목을 제거하고, set으로 출력하세요
items = ["apple", "banana", "apple", "orange", "banana", "grape"]
# 출력 예: {'apple', 'banana', 'orange', 'grape'}
print(set(items))

# 두 집합의 공통 요소 찾기
# 두 집합에서 공통으로 들어있는 요소만 출력하세요.
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}
# 출력 예: {'banana', 'cherry'}
print(set1&set2)

# 집합 차집합 구하기
# 다음 두 집합에서 set1에는 있고 set2에는 없는 요소들을 출력하세요.
set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e"}
# 출력 예: {'a', 'b'}
print(set1-set2)

# 문자열에서 중복 없는 알파벳 개수 세기
# 문자열에서 알파벳만 추출해 set으로 만들고, 총 몇 개의 중복 없는 알파벳이 있는지 출력하세요.
text = "The quick brown fox jumps over the lazy dog!"
# 출력 예: 26
a = ""
for i in text:
  if i.isalpha():
    a += i.lower()
b = set(a)
print(len(b))

#  두 리스트의 공통 항목 찾기
# 다음 두 리스트에서 공통된 항목만 출력하세요. 리스트 → set 변환을 활용해보세요.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
# 출력 예: {4, 5, 6}
a = set(list1)
b = set(list2)
print(a&b)

# 대소문자 구분 없이 알파벳 찾기
# 문자열에서 알파벳만 뽑되, 대소문자를 구분하지 않고 set에 저장하세요.
text = "Python PYTHON pYtHoN"
# 출력 예: {'p', 'y', 't', 'h', 'o', 'n'}
a = text.lower().replace(" ", "")
print(set(a))

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

# 중복 제거하기
# 리스트에 있는 중복 숫자를 제거하고 집합(set)으로 출력하세요.
numbers = [1, 2, 2, 3, 4, 4, 5]
# 출력 예시: {1, 2, 3, 4, 5}
set(numbers)

# 두 집합의 교집합 구하기
# 아래 두 집합에서 공통으로 존재하는 숫자만 출력하세요.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 출력 예시: {3, 4}
print(a&b)

# 차집합 구하기
# a 집합에만 있고, b 집합에는 없는 요소만 출력하세요.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 출력 예시: {1, 2}
print(a-b)

# 학생 출석 체크
# 두 집합이 주어졌을 때, 수업에 출석한 학생들 중 과제를 제출한 학생만 출력하세요.
attended = {"Alice", "Bob", "Charlie", "David"}
submitted = {"Bob", "Charlie", "Eve"}
# 출력 예시: {'Bob', 'Charlie'}
attended & submitted

# 모두 다른 단어 찾기
# 리스트 안에 있는 단어들 중, 중복 없이 한 번만 나온 단어들만 집합으로 출력하세요.
words = ["apple", "banana", "apple", "kiwi", "banana", "peach"]
# 출력 예시: {'kiwi', 'peach'}
a = set()
b = set()

for word in words:
  if word in a:
    b.add(word)
  else:
    a.add(word)
result = a - b
print(result)

# 알파벳 포함 여부 확인
# 문장에서 사용된 알파벳만 집합으로 추출하고, a~z까지 모든 알파벳이 포함되었는지 확인하세요.
sentence = "The quick brown fox jumps over the lazy dog"
# 출력 예시: True  (영문 알파벳 26개가 전부 포함되어 있음)
a = set(char.lower() for char in sentence if char.isalpha())
b = set("abcdefghijklmnopqrstuvwxyz")
print(a == b)

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

# 공통 단어 길이의 평균 구하기
# 두 문장에서 공통으로 등장하는 단어들의 길이 평균을 구하세요. (소문자로 비교)
sentence1 = "Python is a great programming language"
sentence2 = "Learning python language is fun"

s1 = sentence1.lower().split()
s2 = sentence2.lower().split()

# 공통된 단어 추출
a = []
for word in s1:
    if word in s2 and word not in a:
        a.append(word)

# 평균 길이 계산
if len(a) != 0:
    total_a = 0
    for word in a:
        total_a += len(word)
    avr = total_a / len(a)
else:
    avr = 0

print(avr)
