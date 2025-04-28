# 리스트에 숫자 추가하기
# 빈 리스트를 만들고,
#사용자에게 숫자 3개를 입력받아 리스트에 추가한 후 출력하세요.

num = []
for i in range(3):
  a = int(input("숫자 3개 입력하세요:"))
  num.append(a)
print(num)

# 리스트 요소의 합 구하기
# 주어진 리스트 [10, 20, 30, 40]의 모든 요소를 더한 결과를 출력하세요.
a = [10, 20, 30, 40]
print(sum(a))

# 리스트에서 짝수만 추출하기
# 리스트 [1, 2, 3, 4, 5, 6]에서 짝수만 골라 새 리스트로 만들고 출력하세요.
a = [1, 2, 3, 4, 5, 6]
b = [i for i in a if i % 2 == 0]
print(b)

# 리스트에서 최댓값과 최솟값 찾기
# 리스트 [12, 45, 2, 19, 78, 34]가 주어졌을 때,
# 최댓값과 최솟값을 찾아 출력하세요.
numbers = [12, 45, 2, 19, 78, 34]
max_num = max(numbers)
min_num = min(numbers)
print(f"최댓값: {max_num}")
print(f"최솟값: {min_num}")

# 리스트 요소 뒤집기
# 리스트 [1, 2, 3, 4, 5]를
# 거꾸로 뒤집은 새 리스트를 만들어 출력하세요.
a = [1, 2, 3, 4, 5]
b = a[::-1]
print(b)

# 리스트에서 특정 값 개수 세기
# 리스트 ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']에서
# 'apple'이 몇 번 나오는지 세어 출력하세요.
a = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
b = a.count('apple')
print(b)

# 리스트 중 중복 제거 후 오름차순 정렬
# 리스트 [4, 2, 5, 2, 3, 4, 1, 5]가 주어졌을 때,
# 중복을 제거하고 오름차순으로 정렬한 리스트를 출력하세요.
numbers = [4, 2, 5, 2, 3, 4, 1, 5]
# 중복 제거하고 정렬
unique_sorted = sorted(set(numbers))
print(unique_sorted)

# 리스트에서 짝수만 골라 새 리스트 만들기
# 리스트 [10, 15, 20, 25, 30, 35, 40]에서
# 짝수만 골라 새로운 리스트를 만들어 출력하세요.
a = [10, 15, 20, 25, 30, 35, 40]
b = [i for i in a if i % 2 == 0]
print(b)

# 두 리스트 합치기 (중복 없이)
# 두 리스트를 합쳐서, 중복 없이 하나의 리스트로 만들어 출력하세요.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# 두 리스트 합치고 중복 제거
merged = list(set(list1 + list2))
# 정렬까지 하고 싶으면 추가로
merged_sorted = sorted(merged)
print(merged_sorted)

# 문자열 길이 출력
# 사용자에게 문자열을 입력받아, 그 문자열의 길이를 출력하세요.
a = input("입력하세요: ")
print(len(a))

# 문자열 거꾸로 출력
# 사용자에게 문자열을 입력받아,
# 거꾸로 출력하는 프로그램을 작성하세요.
a = input("입력하세요: ")
print(a[::-1])

# 문자열에 특정 문자 개수 세기
# 사용자에게 문자열을 입력받고,
# 그 문자열에 'a' 문자가 몇 개 있는지 세어 출력하세요.
a = input("입력하세요: ")
print(a.count("a"))

# 문자열에서 대소문자 변환
# 주어진 문자열에서 모든 소문자를 대문자로 변환한 결과를 출력하세요.
a = "python"
b = a.upper()
print(b)

# 특정 단어 포함 여부 확인
# 주어진 문자열에 "Python" 이라는 단어가 포함되어 있는지 확인하고,
# 포함되어 있으면 "포함됨", 아니면 "포함되지 않음"을 출력하세요.
a = "I love Python"
b = "Python"
if i in b:
  print("포함됨")
else:
  print("포함안됨")

# 문자열에서 첫 번째와 마지막 글자 추출
# 주어진 문자열에서 첫 번째 글자와 마지막 글자를 출력하세요.
# 예시: "Python" → 첫 글자: P, 마지막 글자: n
a = "Python"
print(f"첫글자:{a[0]}, 마지막글자: {a[-1]}")

# 문자열에서 모든 공백 제거
# 주어진 문자열에서 모든 공백을 제거한 새로운 문자열을 출력하세요.
# 예시: " I love Python " → "IlovePython"
a = " I love Python "
print(a.replace(" ", ""))

# 문자열에서 특정 문자 위치 찾기
# 주어진 문자열에서 **첫 번째 'o'**가 등장하는 인덱스를 찾으세요.
# 만약 없다면 "문자 없음"을 출력하세요.
a = "Python"
print(a.find("o"))

# 문자열에서 단어의 개수 세기
# 주어진 문자열에서 단어의 개수를 출력하세요. 단어는 공백을 기준으로 구분됩니다
a = "I love Python"
b = a.split(" ")
print(len(b))

# 숫자 리스트가 주어졌을 때,
# 짝수만 골라서 새 리스트를 만들어 출력하세요.
def even_thing():
  things = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  a = [i for i in things if i % 2 == 0]
  print(a)
even_thing()

# 문자열에서 모음(a, e, i, o, u)만 골라서 출력하기
def vowels_pop(text):
    vowels = "aeiou"
    result = []
    for i in text:
        if i in vowels:
            result.append(i)
    return result

text = "beautiful day"
print(vowels_pop(text))

# 주어진 리스트에서 중복된 값을 제거하고,
# 중복 없는 리스트를 반환하는 함수 remove_duplicates를 작성하세요.
def remove_duplicates(a):
  return list(set(a))
remove_duplicates([1, 2, 3, 4, 4])

# 주어진 리스트에서 특정 숫자가 몇 번 등장하는지 세는 함수를 작성하세요.
# 함수를 사용하여 주어진 리스트에서 특정 숫자의 등장 횟수를 출력해 보세요.
# my_list = [1, 2, 3, 4, 2, 1, 5, 2, 6]
# target_number = 2
def count_number(my_list, target_number):
  count = 0
  for num in my_list:
    if num == target_number:
      count += 1
  print(f"{target_number}숫자는 {count}번 입니다.")

my_list = [1, 2, 3, 4, 2, 1, 5, 2, 6]
target_number = 2
count_number(my_list, target_number)

# 문제: 리스트에서 짝수만 골라서 새로운 리스트를 만드는 함수 작성하기
# 문제설명: 주어진 리스트에서 짝수만 골라서 새로운 리스트를 만들어 반환하는 함수를 작성하세요.
def get_even_numbers(number):
  a = [i for i in number if i % 2 == 0]
  return a
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_even_numbers(number)

# 최댓값과 최솟값을 동시에 반환하는 함수
# 숫자 리스트를 받아서, 최댓값과 최솟값을 튜플로 반환하는 함수를 작성하세요.
# 조건
# 입력: 숫자 리스트
# 반환: (최댓값, 최솟값) 형태의 튜플
def find_max_min(a):
  b = max(a)
  c = min(a)
  return (b, c)

print(find_max_min([2, 3, 4, 5, 6]))

# 중첩 리스트(flatten) 만들기, 재귀호출문제
# 중첩된 리스트(리스트 안에 리스트)를 받아서,
# 모든 요소를 한 줄(flat)로 만든 새로운 리스트를 반환하는 함수를 작성하세요.
# 조건:
# 입력: 중첩된 리스트
# 반환: 평탄화(flatten)된 리스트
# print(flatten_list([1, [2, 3], [4, [5, 6]]]))
# 출력: [1, 2, 3, 4, 5, 6]
def flatten_list(a):
  b = []
  for i in a:
    if isinstance(i, list):
      b += flatten_list(i)
    else:
      b.append(i)
  return b

print(flatten_list([1, [2, 3], [4, [5, 6]]]))