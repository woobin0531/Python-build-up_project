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

7
# 랜덤 숫자 집합 만들기
# 1부터 10까지의 정수 중에서 서로 다른 숫자 3개를 랜덤하게 뽑아
# 집합(set)으로 만들어 출력하세요.
import random

nums = set(random.sample(range(1, 11), 3))
print(nums)

8
# 랜덤 알파벳 집합 생성
# 알파벳 소문자 중에서 5개를 랜덤하게 뽑아 집합(set)으로 만들고,
# 그 집합의 길이를 출력하세요
import random
import string

letters = set(random.sample(string.ascii_lowercase, 5))
print(letters)
print(len(letters))

9
# 랜덤 리스트에서 중복 제거
# 1부터 5까지의 숫자 중에서 10개를 랜덤하게 뽑아 리스트로 만들고
# 이 리스트에서 중복을 제거한 집합(set)을 출력하세요.
import random

a = [random.randint(1, 5) for i in range(10)]
print(a)
set_a = set(a)
print(set_a)