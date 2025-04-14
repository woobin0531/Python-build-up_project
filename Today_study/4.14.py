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