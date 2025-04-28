1
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

2
#  두 리스트의 공통 항목 찾기
# 다음 두 리스트에서 공통된 항목만 출력하세요. 리스트 → set 변환을 활용해보세요.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
# 출력 예: {4, 5, 6}
a = set(list1)
b = set(list2)
print(a&b)

3
# 대소문자 구분 없이 알파벳 찾기
# 문자열에서 알파벳만 뽑되, 대소문자를 구분하지 않고 set에 저장하세요.
text = "Python PYTHON pYtHoN"
# 출력 예: {'p', 'y', 't', 'h', 'o', 'n'}
a = text.lower().replace(" ", "")
print(set(a))

4
# 학생 출석 체크
# 두 집합이 주어졌을 때, 수업에 출석한 학생들 중 과제를 제출한 학생만 출력하세요.
attended = {"Alice", "Bob", "Charlie", "David"}
submitted = {"Bob", "Charlie", "Eve"}
# 출력 예시: {'Bob', 'Charlie'}
attended & submitted

5
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