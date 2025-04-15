# 1부터 45 사이의 숫자 중 중복 없이 6개를 무작위로 뽑아 리스트로 출력하는 함수를 만들어보세요.
import random

def generate_lotto():
    numbers = random.sample(range(1, 46), 6)  # 중복 없이 6개 뽑기
    return sorted(numbers)

print(generate_lotto())

# 숫자 리스트의 합 구하기
# 주어진 리스트의 모든 숫자를 더한 결과를 출력하세요.
numbers = [3, 5, 1, 8, 2]
print(sum(numbers)

# 리스트에 요소 추가하기
# 리스트에 사용자로부터 입력받은 값을 추가하세요.
# 입력 예시: apple
fruits = ["banana", "cherry"]
fruits.append("apple")
print(fruits)

# 리스트에서 특정 값 제거하기
# 리스트에서 숫자 5를 제거하고 출력하세요.
numbers = [1, 3, 5, 7, 5, 9]
numbers.remove(5)
print(numbers)
numbers.remove(5)
print(numbers)

# 리스트 컴프리헨션 사용
numbers = [1, 3, 5, 7, 5, 9]
numbers = [x for x in numbers if x != 5]

# remove 주의할 점
numbers = [1, 3, 5, 7, 5, 9]
numbers.remove(5)
b = numbers.remove(5)
print(b)

numbers = [1, 3, 5, 7, 5, 9]
numbers.remove(5)      # 첫 번째 5 제거 → numbers = [1, 3, 7, 5, 9]
b = numbers.remove(5)  # 두 번째 5 제거 → numbers = [1, 3, 7, 9]
                       # 하지만 remove는 값을 '제거'만 하고, 아무것도 반환하지 않음
                       # 그래서 b에는 'None'이 들어감

print(b)  # None

# 중복 제거한 리스트 만들기
# 중복된 숫자를 제거하고 새로운 리스트를 만들어 출력하세요.
numbers = [1, 3, 3, 2, 1, 4, 4, 5]
nums = set(numbers)
print(list(nums))

# 짝수만 뽑아 새로운 리스트 만들기
# 주어진 리스트에서 짝수만 골라 새로운 리스트로 만들어 출력하세요.
nums = [10, 13, 17, 20, 24, 29]
a = [x for x in nums if x % 2 == 0]
print(a)

# 리스트의 평균 구하기
# 리스트에 담긴 숫자들의 평균을 구하세요.
scores = [80, 75, 90, 100]
print(sum(scores)/len(scores))

# 단어 길이로 정렬하기
# 아래 리스트를 단어 길이 기준으로 오름차순 정렬하세요.
words = ["banana", "apple", "cherry", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)

# 단어 등장 횟수 세기
# 아래 문장에서 단어별 등장 횟수를 세어 딕셔너리로 출력하세요.
sentence = "apple banana apple cherry banana apple"
a = sentence.split(" ")
a_count = {}
for word in a:
  if word in a_count:
    a_count[word] += 1
  else:
    a_count[word] = 1
print(a_count)

#딕셔너리 컴프리헨션
a_count = {word: a_count(word) for word in set(words)}

# 튜플에서 특정 원소 꺼내기
# 다음 튜플에서 "cherry"를 출력하세요.
fruits = ("apple", "banana", "cherry", "orange")
print(fruits[2])

# 튜플의 길이 출력
# 튜플 (1, 2, 3, 4, 5)의 길이를 출력하세요.
a = (1, 2, 3, 4, 5)
print(len(a))

# 튜플 한 요소만 있는 경우
# 다음 코드에서 변수 t의 자료형은 무엇인가요? 오류가 있으면 고치세요.
t = (5)
print(type(t))  # int
t = (5, )
print(type(t))  # tuple

# 튜플에서 값 찾기
# 다음 튜플에서 값이 20인 인덱스를 모두 찾아 리스트로 출력하세요.
nums = (10, 20, 30, 20, 40, 20)
index = [x for x, v in enumerate(nums) if v == 20]
print(index)

# 튜플 언패킹
# 다음 튜플을 언패킹해서 변수 a, b, c에 각각 저장하고 출력하세요.
t = (100, 200, 300)
a, b, c = t
print(a, b, c)

# 튜플 정렬
# 다음 튜플을 정렬하여 리스트로 출력하세요.
t = (5, 1, 9, 3)
print(list(sorted(t)))

# 튜플로 구성된 리스트 정렬 (두 번째 요소 기준)
# 아래 리스트를 두 번째 요소 기준으로 오름차순 정렬하세요.
data = [("a", 3), ("b", 1), ("c", 2)]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)

# 튜플 리스트에서 최대값 찾기
# 아래 튜플 리스트에서 가장 점수가 높은 학생의 이름을 출력하세요.
scores = [("John", 88), ("Alice", 92), ("Bob", 85)]
top_scores = max(scores, key=lambda x: x[1])
print(top_scores)

# 튜플에서 중복 제거
# 아래 튜플에서 중복된 값을 제거하고 튜플로 반환하세요.
t = (1, 2, 2, 3, 1, 4)
unique_t = tuple(set(t))
print(unique_t)

# 문자열 길이 구하기
# 주어진 문자열의 길이를 출력하세요.
text = "Python"
print(len(text))

# 첫 글자와 마지막 글자 출력하기
# 문자열의 첫 글자와 마지막 글자를 출력하세요.
word = "Programming"
print(word[0],word[-1])

# 문자열 일부 추출하기
# "I love Python"에서 "love"만 추출해서 출력하세요.
sentence = "I love Python"
print(sentence[2:6])

# 대소문자 바꾸기
# 주어진 문자열에서 대문자는 소문자로, 소문자는 대문자로 바꿔서 출력하세요.
text = "PyTHon Is FuN"
print(text.swapcase())

result = ""
for i in text:
  if i.isupper():
    result += i.lower()
  elif i.islower():
    result += i.upper()
  else:
    result += i
print(result)

# 단어 개수 세기
sentence = "Life is short, you need Python"
print(len(sentence.split()))

# 거꾸로 출력하기
# 문자열을 거꾸로 뒤집어서 출력하세요.
word = "developer"
print(word[::-1])

# 가장 많이 등장한 문자 찾기
# 문자열에서 가장 많이 등장한 알파벳(공백 제외)을 찾아 출력하세요.
# 대소문자는 구분하지 않습니다.
text = "Simple is better than complex"
b =text.lower().replace(" ", "")
c = {}
for i in b:
  if i in c:
    c[i] += 1
  else:
    c[i] =1
d = 0
e = None
for i, count in c.items():
  if count > d:
    e = i
    d = count
print(e)

# 특정 단어 제거
# 주어진 문장에서 특정 단어만 제거하고 출력하세요.
# "the"라는 단어만 제거해야 하며, 대소문자 구분 없이 동작해야 합니다.
sentence = "The quick brown fox jumps over the lazy dog"
word_to_remove = "the"

# 공백 기준으로 단어 하나씩 직접 처리
words = sentence.split()
result = []

for word in words:
    if word.lower() != word_to_remove.lower():
        result.append(word)

# 다시 문자열로 합치기
new_sentence = ""
for i in range(len(result)):
    new_sentence += result[i]
    if i < len(result) - 1:  # 마지막 단어가 아니라면, 그 뒤에 공백 하나를 붙여야하므로
        new_sentence += " "  # 이걸 안하면 "quickbrownfox" 처럼 단어가 붙어버림

print(new_sentence)  # 출력: "quick brown fox jumps over lazy dog"

sentence = "The quick brown fox jumps over the lazy dog"
word_to_remove = "the"
sentence = ' '.join([word for word in sentence.split() if word.lower() != word_to_remove.lower()])

print(sentence)  # 출력: "quick brown fox jumps over lazy dog"

# 값 접근하기
# 주어진 딕셔너리에서 "name"에 해당하는 값을 출력하세요.
person = {"name": "Alice", "age": 25, "city": "Seoul"}
print(person["name"])

# 키-값 추가하기
# 딕셔너리에 "job"이라는 키와 "Developer"라는 값을 추가하세요.
person = {"name": "Bob", "age": 30}
person["job"] = "Developer"
print(person)

# 모든 키 출력하기
# 아래 딕셔너리에서 모든 키를 하나씩 출력하세요.
fruits = {"apple": 3, "banana": 5, "orange": 2}
print(fruits.keys())

fruits = {"apple": 3, "banana": 5, "orange": 2}
for key in fruits:
    print(key)

# # 아래 딕셔너리에서 "age" 값을 40으로 변경하세요.
person = {"name": "Charlie", "age": 28, "city": "Busan"}
person["age"]=40
print(person)

# 값 기준으로 조건 출력하기
# 점수가 80점 이상인 학생들만 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
good_scores = {}
for key,value in scores.items():
  if value >= 80:
    good_scores[key] = value
print(good_scores)

# 딕셔너리에서 최대값 찾기
# 아래 딕셔너리에서 가장 비싼 과일의 이름을 출력하세요.
prices = {"apple": 1200, "banana": 800, "mango": 1500, "peach": 1000}
max_price = 0
max_fruit = ""
for fruit,price in prices.items():
  if price > max_price:
    max_price = price
    pmax_fruit = fruit
print(max_fruit)
# 한줄
print(max(prices, key=prices.get))

#: 키 중복 없이 병합하기
# 아래 두 딕셔너리를 병합하되, key가 중복되면 기존 값을 유지하세요.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
i = dict1.copy()
for key in dict2:
  if key not in i:
    i[key] = dict2[key]
print(i)

# 딕셔너리 값 기준 정렬
# 아래 딕셔너리를 점수 기준으로 내림차순 정렬하여 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 90}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)

# 리스트를 딕셔너리로 변환
# 아래 두 리스트를 이용해 학생 이름을 키로, 점수를 값으로 하는 딕셔너리를 만드세요.
names = ["Eve", "Frank", "Grace"]
scores = [88, 76, 95]
student_scores = {}
for i in range(len(names)):
  student_scores[names[i]] = scores[i]
print(student_scores)

# 중복 제거
# 아래 리스트에서 중복된 값을 제거하고 set으로 만드세요.
numbers = [1, 2, 2, 3, 4, 4, 5]
a = set(numbers)
print(a)

# 값 추가
# 아래 set에 숫자 10을 추가하세요.
my_set = {1, 2, 3}
my_set.add(10)
print(my_set)

# 특정 값 제거
# 아래 set에서 숫자 3을 제거하세요.
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)

# 교집합 구하기
# 두 집합의 공통된 요소만 출력하세요.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)

# 차집합 구하기
# 집합 a에서 b에 없는 값만 출력하세요.
a = {1, 2, 3, 4, 5}
b = {3, 4, 6}
print(a-b)

# 중복 없는 알파벳 개수 세기
# 문자열에서 중복 없이 사용된 알파벳의 개수를 출력하세요.
text = "hello world"
a = text.replace(" ", "")
set(a)
len(set(a))

# 대소문자 구분 없이 알파벳 중복 제거
# 아래 문자열에서 대소문자를 구분하지 않고 알파벳만 중복 없이 뽑아 set으로 만드세요.
sentence = "The Quick Brown Fox jumps Over the Lazy Dog!"
a =sentence.lower().replace("!", "").replace(" ", "")
print(set(a))

sentence = "The Quick Brown Fox jumps Over the Lazy Dog!"
result = set()
for ch in sentence.lower():
  if ch.isalpha():
    result.add(ch)
print(result)

# 공통 요소가 없는지 확인하기
# 아래 두 집합에 공통된 요소가 없으면 True, 있으면 False를 출력하세요.
x = {1, 3, 5}
y = {2, 4, 6}
if x & y :
  print(True)
else:
  print(False)

# 랜덤 정수 생성
# 1부터 10 사이의 랜덤한 정수를 출력하세요.
import random
print(random.randint(1,10))

# 리스트에서 랜덤 선택
# 아래 리스트에서 무작위로 하나를 골라 출력하세요.
import random
fruits = ["apple", "banana", "cherry", "mango"]
food = random.choice(fruits)
print(food)

# 리스트 섞기
# 아래 리스트의 순서를 무작위로 섞은 후 출력하세요.
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  #리스트의 요소를 무작위로 섞어, 직접 리스트를 바로 변경하는 함수
print(numbers)

# 랜덤 비밀번호 생성기
# 소문자 알파벳 중에서 랜덤하게 8글자로 구성된 비밀번호를 만들어 출력하세요.
import random
import string
password = ""
for i in range(8):
  password += random.choice(string.ascii_lowercase+string.digits)
print(password)

# 중복 없이 로또 번호 생성
import random

lotto = random.sample(range(1, 46), 6)  # 1~45 중 중복 없이 6개
lotto.sort()
print(lotto)

# 랜덤한 퀴즈 문제 출제기
# 아래 리스트에서 랜덤하게 하나의 질문을 출력하세요.
import random

questions = [
    "파이썬의 창시자는?",
    "파이썬에서 리스트를 만드는 방법은?",
    "변수를 선언할 때 사용하는 기호는?",
    "if문은 어떤 상황에서 쓰나요?"
]

quiz = random.choice(questions)
print("오늘의 랜덤 퀴즈:", quiz)
