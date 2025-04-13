#반복 가능한 객체(literable)이란?
-즉 하나씩 거낼 수 있는 객체
-for 문으로 돌릴 수 있는 것들

#sep는  print() 함수 안에서 사용하는 매개변수
-sep 의 기본값이 ' '
print("안녕", "우빈", "파이썬", sep='★') # 안녕★우빈★파이썬

#end는 줄 끝에 넣을 문자 설정
-기본 값: '\ n'
print("우빈", end="!!!")
print("짱")  # 우빈!!!짱

# t.index(2, 시작위치)

#언패킹(unpacking)은 묶여 있는 자료(예: 튜플, 리스트 등)를 각각의 변수로 푸는 작업
-변수 개수 ≠ 요소 개수 → 오류

#시퀀스(Sequence)는 순서가 있는 자료형.
#쉽게 말해서 인덱스(index)로 각 요소에 접근할 수 있는 자료형

#split()은 리스트를 반환 (문자열을 split하면 리스트로 반환)

#s3 = set("hello")    # 문자열 → {'h', 'e', 'l', 'o'}
-문자 하나하나가 원소로 들어간 집합이 됨

#s = {1, 2, (3, 4)}  # ✅ 튜플은 가능
# s = {1, 2, [3, 4]}  → ❌ 리스트는 불가능 (mutable)

import random
for _ in range(10):
    print(random.random())

#주사위를 100번 굴렸다고 가정하고,
#각 숫자(1~6)가 몇 번 나왔는지 세어보세요.
import random
counts = {i: 0 for i in range(1, 7)}  # 1~6가지 초기화
for _ in range(100):
  roll = random.randint(1, 6)
  counts[roll] += 1
print(counts)

import random
options = ['가위', '바위', '보']
user = input("가위, 바위, 보 중 하나 입력: ")
computer = random.choice(options)

print(f"컴퓨터: {computer}")
if user == computer:
    print("비겼습니다!")
elif (user == '가위' and computer == '보') or \
     (user == '바위' and computer == '가위') or \
     (user == '보' and computer == '바위'):
    print("당신이 이겼습니다!")
else:
    print("컴퓨터가 이겼습니다!")

