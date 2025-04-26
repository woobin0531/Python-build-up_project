# 랜덤 숫자 맞추기 게임 (컴퓨터가 고른 숫자 맞추기)
# 문제: 1부터 50 사이의 랜덤 숫자 하나를 생성하고,
# 사용자가 입력한 숫자와 비교하여 높은지, 낮은지를 알려주는 로직을 만들어보세요.
# 사용자가 맞힐 때까지 반복합니다.
import random

target = random.randint(1, 50)

while True:
    guess = int(input("숫자를 입력하세요 (1~50): "))
    if guess < target:
        print("더 큰 숫자입니다.")
    elif guess > target:
        print("더 작은 숫자입니다.")
    else:
        print("정답입니다!")
        break

# 로또 번호 생성기
# 문제:1부터 45 사이의 숫자 중 중복 없이 6개의 숫자를 무작위로 선택하여 오름차순으로 출력하세요.
import random

lotto = random.sample(range(1, 46), 6)
lotto.sort()
print(lotto)

# 리스트에서 랜덤하게 요소 3개 제거하기
# 문제: 임의의 리스트가 있을 때, 그 중 3개의 요소를 랜덤하게 제거한 뒤 남은 리스트를 출력하세요.
# 단, 리스트 길이는 최소 6 이상이어야 합니다.
# 예시 리스트: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
import random

ex_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
to_remove = random.sample(ex_list, 3)
for item in to_remove:
    ex_list.remove(item)

print(ex_list)


# 문제: 세 수 중 가장 큰 수 찾기
# 정수 3개를 입력받아, 가장 큰 수를 반환하는 함수를 작성하세요.
# 함수 이름: find_max
# 입력: 세 개의 정수
# 반환: 가장 큰 수 (정수)
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(2, 3, 4))

# 문자열 길이 구하기
# 문자열 하나를 입력받아, 그 문자열의 길이를 반환하는 함수를 작성하세요.
# 함수 이름: string_length
# 입력: 문자열 1개
# 반환: 문자열의 길이 (정수)
def string_length(a):
  return len(a)

string_length("hello")

# 리스트 요소 합계 구하기
# 정수로 이루어진 리스트를 입력받아, 요소들의 합을 반환하는 함수를 작성하세요.
# 함수 이름: list_sum
# 입력: 정수 리스트
# 반환: 합계 (정수)
def list_sum(a):
  return sum(a)
print(list_sum([1, 2, 3, 4]))

# 문자열 뒤집기
# 문자열 하나를 입력받아, 거꾸로 뒤집은 문자열을 반환하는 함수를 작성하세요.
# 함수 이름: reverse_string
# 입력: 문자열 1개
# 반환: 뒤집힌 문자열
def reverse_string(a):
  return a[::-1]
print(reverse_string("hello"))

# 리스트에서 짝수만 추출
# 정수 리스트를 입력받아, 짝수만 모은 새 리스트를 반환하는 함수를 작성하세요.
# 함수 이름: get_even_numbers
# 입력: 정수 리스트
# 반환: 짝수만 담긴 리스트
def get_even_numbers(a):
  return [num for num in a if num % 2 == 0]
print(get_even_numbers([1, 2, 3, 4, 5]))

# 단어 개수 세기
# 문자열 하나를 입력받아, 그 안에 있는 단어(word) 의 개수를 반환하는 함수를 작성하세요.
# (단어는 띄어쓰기로 구분합니다.)
# 함수 이름: count_words
# 입력: 문자열 1개
# 반환: 단어 개수 (정수)
def count_words(s):
  a =s.split(" ")
  return len(a)
print(count_words("I love Python") )

# 중복 제거 후 정렬
# 리스트를 입력받아, 중복을 제거하고 오름차순으로 정렬한 새 리스트를 반환하는 함수를 작성하세요.
# 함수 이름: remove_duplicates_and_sort
# 입력: 리스트 (숫자 또는 문자열)
# 반환: 중복 없이 정렬된 리스트
def remove_duplicates_and_sort(a):
  b = sorted(set(a))
  c = list(b)
  return c
print(remove_duplicates_and_sort([1, 2, 3, 3, 4]))

# 팩토리얼 계산
# 양의 정수 하나를 입력받아, 그 수의 팩토리얼을 반환하는 함수를 작성하세요.
# (팩토리얼: n! = n × (n-1) × (n-2) × ... × 1)
# 함수 이름: factorial
# 입력: 양의 정수 1개
# 반환: 팩토리얼 값 (정수)
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
print(factorial(5))

# 리스트를 문자열로 변환
# 문자열 리스트를 입력받아, 콤마(,)로 연결된 하나의 문자열로 반환하는 함수를 작성하세요.
# 함수 이름: list_to_string
# 입력: 문자열 리스트
# 반환: 하나의 문자열
def list_to_string(a):
  b = ",".join(a)
  return b
print(list_to_string(["a", "b", "c"]))

# 1부터 5까지 출력
# while문을 사용해서 1부터 5까지 차례대로 출력하는 코드를 작성하세요.
i = 1
while i <= 5:
  print(i)
  i += 1

# 10부터 1까지 거꾸로 출력
# while문을 사용해서 10부터 1까지 거꾸로 출력하는 코드를 작성하세요.
i = 10
while i >= 1:
    print(i)
    i -= 1

# 합이 50 이상이 될 때까지 숫자 더하기
# 1부터 시작해서 숫자를 하나씩 더해가면서,
# 합이 50 이상이 되는 순간 멈추는 코드를 while문으로 작성하세요.
# (현재까지의 합도 같이 출력하기)
i = 1
total = 0

while total < 50:
    total += i
    i += 1

print(total)

# 1부터 100 사이의 짝수만 출력
# while문을 사용해서 1부터 100까지 중에서 짝수만 출력하세요.
i = 1
even = []
while i <= 100:
    if i % 2 == 0:
        even.append(i)
    i += 1

print(even)


# 숫자 맞히기 게임
# 1부터 10 사이의 랜덤 숫자 하나를 정해놓고,
# 사용자가 숫자를 입력하면서 맞힐 때까지 계속 물어보는 프로그램을 작성하세요.
# (힌트: 맞으면 "정답!" 출력하고 종료)
import random

computer = random.randint(1, 10)

while True:
    a = int(input("숫자를 입력하세요(1~10): "))
    if computer == a:
        print("정답!")
        break
    else:
        print("틀렸습니다. 다시 시도하세요.")

# 문자열 뒤집기
# 문자열을 입력받아서,
# while문을 사용해 문자열을 뒤집은 결과를 출력하세요.
s = input("문자열을 입력하세요: ")  #hello
reversed_s = ''
i = len(s) - 1  # 4

while i >= 0:
    reversed_s += s[i]  #o
    i -= 1 # 3

print(reversed_s)

# 1부터 10까지 출력
# while문을 사용해서 1부터 10까지 숫자를 출력하세요.
i = 1
while i <= 10:
  print(i)
  i += 1

# 1부터 10까지 합 구하기
# while문을 사용해서 1부터 10까지 숫자의 합을 구하고 출력하세요.
i = 1
total = 0
while i <= 10:
  total += i
  i += 1

print(total)

# "hello"를 5번 출력
# while문을 사용
a = "hello"
count_a = 0
while count_a < 5:
  print(a)
  count_a += 1

# 1부터 100까지 짝수의 합 구하기
# while문을 사용해서 1부터 100까지 숫자 중 짝수만 더해서 총합을 출력하세요.
i = 2
total_even = 0

while i <= 100:
  total_even += i
  i += 2
print(total_even)

# 1부터 n까지 3의 배수 출력
# 사용자에게 n을 입력받고,
# while문으로 1부터 n까지 중 3의 배수만 출력하세요.
def a(n):
  i = 1
  ii = []
  while i <= n:
    if i % 3 ==0:
      ii.append(i)
    i += 1
  return ii
print(a(100))

# 입력한 수까지 거꾸로 출력
# 사용자에게 정수 하나를 입력받고,
# while문으로 그 숫자부터 1까지 거꾸로 출력하세요.
a = int(input("숫자를입력하세요: "))

while a >= 1:
  print(a)
  a -= 1