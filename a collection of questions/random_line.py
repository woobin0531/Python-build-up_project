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