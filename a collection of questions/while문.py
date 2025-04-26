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