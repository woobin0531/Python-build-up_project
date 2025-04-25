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

#join
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