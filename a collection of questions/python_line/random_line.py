# 랜덤 숫자 생성하기
# 문제: 1부터 100 사이의 정수 중 하나를 랜덤으로 출력하세요.
import random
a = random.randint(1, 100)
print(a)

# 리스트에서 랜덤 선택
# 문제: 아래 리스트에서 무작위로 하나의 과일을 선택해 출력하세요.
import random
fruits = ["apple", "banana", "cherry", "grape", "mango"]
a = random.choice(fruits)
print(a)

# 리스트 섞기
# 문제: 아래 리스트를 무작위로 섞은 후 출력하세요.
numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
print(numbers)

# 랜덤 비밀번호 생성기
# 문제: 영문자(대소문자), 숫자, 특수문자 중에서 무작위로 섞어서
# 길이 8자리의 비밀번호를 만들어 출력하세요.
# 사용 가능한 문자들:
# 영문자: a-z, A-Z
# 숫자: 0-9
# 특수문자: !@#$%^&*
import random
import string
letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*"
all_things = letters + digits + symbols

password = ''.join(random.choices(all_things, k=8))
print(password)

# 가위바위보 게임
# 문제: 사용자에게 '가위', '바위', '보' 중 하나를 입력받고,
# 컴퓨터는 무작위로 선택합니다.
# 누가 이겼는지 결과를 출력하세요.

# 예시:
# 사용자: 가위
# 컴퓨터: 보
# 결과: 사용자 승!
import random

유저 = input("가위/바위/보 선택해주세요: ")
use = ['가위', '바위', '보']
computer = random.choice(use)

if 유저 == computer:
  result = "비겼습니다"
elif (유저 == '가위' and computer == '보')or \
  (유저 == '바위' and computer == '가위') or \
  (유저 == '보' and computer == '바위'):
  result = "사용자 승!"
else:
  result = "컴퓨터 승!"
print(f"사용자: {유저}")
print(f"컴퓨터: {computer}")
print(f"결괴: {result}")

# 주사위 숫자 출력하기
# 문제: 1부터 6까지의 숫자 중 하나를 무작위로 출력하세요.
# 조건: random 모듈을 사용하세요.
# 숫자는 정수형으로 출력되어야 합니다.
import random

print(random.randint(1, 6))

# 3개의 랜덤 숫자 리스트 만들기
# 문제: 0부터 9까지의 숫자 중에서 중복 없이 3개를 무작위로 골라 리스트로 만드세요.
# 조건: random.sample() 사용 가능
# 출력 예시: [3, 7, 1]
import random

numbers = random.sample(range(10), 3)
print(numbers)

# 랜덤 글자 선택하기
# 문제: 문자열 "abcdefg"에서 임의의 한 글자를 무작위로 출력하세요.
# 조건:random.choice() 사용 가능
# 출력 예시: 'e'
import random

s = "abcdefg"
char = random.choice(s)
print(char)

# 1부터 100 사이의 숫자 중 짝수만 5개 뽑기
# 문제: 1부터 100 사이의 숫자 중 짝수만 골라서 그 중 무작위로 5개를 선택하여 출력하세요.
import random

evens = [i for i in range(2, 101, 2)]
random_evens = random.sample(evens, 5)
print(random_evens)

# 랜덤한 4자리 숫자 만들기
# 문제: 0부터 9까지 숫자 중에서 중복 없이 4개를 골라
# 하나의 문자열 형태로 이어진 4자리 숫자를 만드세요. 예: "5812"
import random

a = random.sample(range(10), 4)
b = ''.join(str(i) for i in a)
print(b)

# 리스트 섞기
# 문제: 다음 리스트를 무작위로 섞은 결과를 출력하세요.
# 리스트: ["apple", "banana", "cherry", "date"]
import random
fruits = ["apple", "banana", "cherry", "date"]
random.shuffle(fruits)
print(fruits)