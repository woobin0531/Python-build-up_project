#정수 n을 입력하고 n까지의 짝수의 합

a = int(input())
score = 0
for i in range(1, a+1):
  if i % 2 == 0:
    score += i
print(score)