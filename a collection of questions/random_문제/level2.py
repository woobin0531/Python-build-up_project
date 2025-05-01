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

4
# 랜덤 실수 생성 및 반올림
# random 모듈을 사용하여 1 이상 100 미만의 실수(float)를 하나 생성하고
# 소수점 둘째 자리까지 반올림해서 출력하세요.
import random
a = random.uniform(1, 100)
print(round(a, 2))

5
# 리스트 섞기와 슬라이싱
# 1부터 10까지의 숫자로 이루어진 리스트를 랜덤하게 섞은 뒤
# 앞에서 3개만 출력하세요.
import random

a = list(range(1, 11))
random.shuffle(a)
b = a[:3]
print(b)

6
# 랜덤 추첨 프로그램
# 아래와 같이 10명의 이름이 들어 있는 리스트가 있습니다.
# 이 중에서 3명을 중복 없이 무작위로 뽑아 출력하는 코드를 작성하세요.
names = ['철수', '영희', '민수', '지민', '수진', '현우',
         '나영', '준호', '예린', '다은']
sample_names = random.sample(names, 3)
print(sample_names)