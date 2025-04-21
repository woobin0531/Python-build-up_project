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