# 1부터 n까지 홀수의 합 구하기
# 사용자에게 n을 입력받고,
# while문을 사용해 1부터 n까지 홀수만 더한 합을 출력하세요.
a = int(input())
i = 1
sum_a = 0

while i <= a:
    sum_a += i
    i += 2

print(sum_a)

# 특정 문자열 거꾸로 출력
# 문자열을 입력받아,
# while문을 사용해서 한 글자씩 거꾸로 출력하세요.
# (ex: 입력 "apple" → 출력 "e", "l", "p", "p", "a")
text = input("문자를 입력해주세요: ")
i = len(text) - 1

while i >= 0:
  print(text[i])
  i -= 1

# n부터 0까지 3씩 감소하며 출력
# 사용자에게 n을 입력받고,
# while문으로 n부터 0까지 3씩 감소시키면서 숫자를 출력하세요.
# (ex: n=10이면 10, 7, 4, 1 순으로 출력)
a = int(input("숫자를 입력해주세요: "))
b = []
while a >= 0:
  print(a)
  a -= 3

# 1부터 n까지의 합 구하기
# 사용자에게 양의 정수 n을 입력받고,
# while문을 사용해서 1부터 n까지의 총합을 구해서 출력하세요.
a = int(input())
sum_a = 0
i = 1

while i <= a:
  sum_a += i
  i += 1
print(sum_a)

# 입력한 숫자들의 평균 구하기
# 사용자에게 숫자를 계속 입력받다가,
# 입력값이 -1이면 입력을 종료하고,
# 지금까지 입력한 숫자들의 평균을 구해서 출력하세요.

b = 0
c = 0

while True:
  a = int(input("숫자를 입력해주세요(종료는 -1): "))
  if a == -1:
    break
  b += a
  c += 1

if c == 0:
  print("입력 숫자가 없습니다.")
else:
  avr = b / c
  print(f"평균은 {avr}입니다.")

# 5의 배수 찾기
# 사용자에게 양의 정수 n을 입력받고,
# while문을 사용해서 1부터 n까지 중에서 5의 배수만 출력하세요.
a = int(input())
i = 1

while i <= a:
  if i % 5 == 0:
    print(i)
  i += 1