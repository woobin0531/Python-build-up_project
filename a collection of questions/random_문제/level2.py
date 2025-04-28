1
# 1부터 100 사이의 숫자 중 짝수만 5개 뽑기
# 문제: 1부터 100 사이의 숫자 중 짝수만 골라서 그 중 무작위로 5개를 선택하여 출력하세요.
import random

evens = [i for i in range(2, 101, 2)]
random_evens = random.sample(evens, 5)
print(random_evens)

2
# 랜덤한 4자리 숫자 만들기
# 문제: 0부터 9까지 숫자 중에서 중복 없이 4개를 골라
# 하나의 문자열 형태로 이어진 4자리 숫자를 만드세요. 예: "5812"
import random

a = random.sample(range(10), 4)
b = ''.join(str(i) for i in a)
print(b)

3
# 리스트 섞기
# 문제: 다음 리스트를 무작위로 섞은 결과를 출력하세요.
# 리스트: ["apple", "banana", "cherry", "date"]
import random
fruits = ["apple", "banana", "cherry", "date"]
random.shuffle(fruits)
print(fruits)