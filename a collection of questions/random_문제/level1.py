1
# 랜덤 숫자 생성하기
# 문제: 1부터 100 사이의 정수 중 하나를 랜덤으로 출력하세요.
import random
a = random.randint(1, 100)
print(a)

2
# 리스트에서 랜덤 선택
# 문제: 아래 리스트에서 무작위로 하나의 과일을 선택해 출력하세요.
import random
fruits = ["apple", "banana", "cherry", "grape", "mango"]
a = random.choice(fruits)
print(a)

3
# 리스트 섞기
# 문제: 아래 리스트를 무작위로 섞은 후 출력하세요.
numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
print(numbers)

4
# 주사위 숫자 출력하기
# 문제: 1부터 6까지의 숫자 중 하나를 무작위로 출력하세요.
# 조건: random 모듈을 사용하세요.
# 숫자는 정수형으로 출력되어야 합니다.
import random

print(random.randint(1, 6))

5
# 3개의 랜덤 숫자 리스트 만들기
# 문제: 0부터 9까지의 숫자 중에서 중복 없이 3개를 무작위로 골라 리스트로 만드세요.
# 조건: random.sample() 사용 가능
# 출력 예시: [3, 7, 1]
import random

numbers = random.sample(range(10), 3)
print(numbers)

6
# 랜덤 글자 선택하기
# 문제: 문자열 "abcdefg"에서 임의의 한 글자를 무작위로 출력하세요.
# 조건:random.choice() 사용 가능
# 출력 예시: 'e'
import random

s = "abcdefg"
char = random.choice(s)
print(char)