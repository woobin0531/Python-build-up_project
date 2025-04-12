#아래와 같은 문장이 주어졌을 때,
#각 단어가 몇 번씩 등장했는지를 나타내는 딕셔너리를 만들어 출력하세요.
#단, 대소문자는 구분하지 않고, 특수문자는 모두 제거한 뒤 계산하세요.
text = "Python is great, and Python is easy to learn. Isn't Python amazing?"
a = text.lower()
a = a.replace(',', '').replace('?', '').replace("'", '')
words = a.split()
b = {}
for item in words:
  if item in b:
    b[item] += 1
  else:
    b[item] = 1
print(b)

#단어 빈도수 분석기
"""
입력은 한 줄의 문장입니다.
문장에는 알파벳 소문자와 대문자, 그리고 일부 구두점(.,!?')이 포함될 수 있습니다.
대소문자는 구분하지 않으며, 모두 소문자로 처리합니다.
단어는 공백 기준으로 나뉩니다.
"""
def sort_key(item):
  return (-item[1], item[0])

a = input("문장을 입력하세요: ")
a = a.lower().replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace("'", '')
b = a.split()
c = {}
for word in b:
  if word in c:
    c[word] += 1
  else:
    c[word] = 1

sorted_items = sorted(c.items(), key=sort_key)
sorted_c = dict(sorted_items)
most_common = sorted_items[0][0]
print(f"가장 많이 등장한 단어: {most_common} ({c[most_common]}회)")
print("\n등장 횟수 순 정렬:")
print(sorted_c)

#사용자가 입력한 문장에서 단어의 등장 횟수를 세고,
#단어의 길이와 알파벳 순서 기준으로 정렬해서 출력하세요.
a = input("문장을 입력해주세요:")
a = a.lower().replace(".", "").replace(",", "").replace("!", "")
b = a.split()
c = {}
for word in b:
  if word in c:
    c[word] += 1
  else:
    c[word] = 1
sorted_items = sorted(c.items(), key=lambda item: (-item[1], item[0])) #lambda 로 정렬: (등장 횟수 내림차순, 단어 오름차순)
sorted_c = dict(sorted_items)
most_common = sorted_items[0][0]
print(f"가장 많이 등장한 단어: {most_common} ({c[most_common]}회)")
print(sorted_c)

#단어별 자음 개수로 정렬하기
'''
문장 부호를 제거하고,
모든 단어를 소문자로 바꾸고,
각 단어에 들어 있는 자음(consonant)의 개수를 센 다음,
자음 개수 기준으로 내림차순 정렬하세요.
자음 개수가 같으면 단어 길이가 더 긴 단어를 먼저 출력하세요.
'''
consonants = 'bcdfghjklmnpqrstvwxyz'  #자음모음
a = input("문장을 입력하세요:")
a = a.lower().replace(".", "").replace(",", "")
words = a.split()
sorted_words = sorted(
    words, key=lambda word: (
        -sum(1 for ch in word if ch in consonants),
        -len(word)
    )
)
print("자음 개수 기준 정렬 결과:")
for word in sorted_words:
  consonant_count = sum(1 for ch in word if ch in consonants)
  print(f"{word} ({consonant_count}자음)")

#가장 긴 단어 그룹 찾기 (dict, lambda, sorted, filter, split, replace, lower )
'''
사용자가 문장을 입력하면:
문장 부호를 제거하고,
모든 단어를 소문자로 변환한 후,
단어들을 길이 기준으로 묶는다
가장 긴 길이를 가진 단어들만 출력
'''
a = input("문장을입력하세요: ")
a = a.lower().replace(",", "").replace(".", "").replace("!", "")
b = a.split()
unique_words = list(set(b))  # 중복 제거, 순서
sorted_words = sorted(unique_words, key=lambda x: len(x), reverse=True)  #단어 길이 정렬
max_length = len(sorted_words[0])
longest_words = list(filter(lambda x: len(x) == max_length, sorted_words))
longest_words.sort()
print(f"가장 긴 단어의 길이: {max_length}")
print(longest_words)

# lambda 함수
'''- 한줄로 간단하게 표현할 수 잇는 "익명 함수(함수 이름 없이 만드는 함수)"
- lambda 매개변수: 표현식
ex) 
lambda x: x + 1 는 
def add_one(x):
  return x + 1 랑 같다.
- 보통은 정렬하거나, 필터링, 맵핑 할 때 간단한 함수를 임시로 쓰고 싶을 때 사용
'''
#lambda 함수를 사용해서, 아래 문자열 리스트를 문자열 길이 기준으로 오름차순 정렬해보세요.
words = ["kiwi", "apple", "banana", "cherry"]
words_sorted = sorted(words, key=lambda x: len(x))
print(words_sorted)

students = [("영희", 90), ("철수", 80), ("민수", 95)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

is_even = lambda x: "짝수" if x % 2 == 0 else "홀수"
print(is_even(4))

#map()함수
'''
map(함수, 반복 가능한 자료형)
-리스트나 튜플 같은 반복 가능한 자료형의 각 요소에 함수를 작용해서 새로운 결과를 만들어주는 함수
'''
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

def upper_case(word):
  return word.upper()
words = ['hello', 'world']
result = list(map(upper_case, words))
print(result)

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)

#filter()함수
'''
filter(function, iterable)
-iterable(리스트, 튜플, 문자열 등)에서
function 을 각 요소에 적용해서
True인 값만 필터링(걸러내서) 새로 반환
-반한되는 건 filter 객체니까 보통 list()나 tuple()로 감싸서 쓴다.
'''
result = filter(lambda x: x > 0, [-1, 0, 1, 2])
print(result)  # filter object
print(list(result))  # [1, 2]
'''
그냥 print(result) 하면 필터 객체 주소만 보여줘.
반드시 list()나 tuple()로 자료형 변환해서 써야 됨!
'''

#할 일 목록 자동 정리기
'''
사용자가 입력한 할 일(To-Do) 목록에서
각 항목을 중요도에 따라 정리하고,
중복된 항목은 제거해서 우선순위대로 정렬된 리스트를 보여주세요
'''
tasks = [
    ("청소하기", 2),
    ("운동하기", 1),
    ("장보기", 3),
    ("청소하기", 2),
    ("독서하기", 1),
    ("운동하기", 1),
]
task_dict = {}
for task, priority in tasks:
  if task in task_dict:
    task_dict[task] = min(task_dict[task], priority)
  else:
    task_dict[task] = priority
sorted_tasks = sorted(task_dict.items(), key=lambda x: x[1])
print(sorted_tasks)