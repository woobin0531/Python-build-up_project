# random 함수


#random.seed()
-랜덤값 생성을 위한 초기값(seed)을 설정.
-같은 seed 값을 주면 항상 같은 난수 결과
-주로 디버깅, 테스트, 예측 가능한 결과가 필요할 때 사용
import random
random.seed(42)
print(random.randint(1, 100))  # 82
print(random.random())  #0.63942...

#getstate(): 난수 생성기의 상태를 저장해서 나중에 똑같은 난수 시퀀스를 다시 생성할 수 있도록 해주는 함수
import random
state = random.getstate()
print(random.randint(1,100)) #23
random.setstate(state)
print(random.randint(1,100))  #23

#getrandbits(k): k비트 크기의 무작위 정수(0이상)를 생성하는 함수
import random
num = random.getrandbits(4)
print(num)  # 7

#random.randrange(): 지정된 범위 내에서 정수를 무작위로 하나 반환하는 함수
import random
print(random.ranfrange(10))  #0~9 중 하나 출력

#randint(): 지정된 두 정수 사이에서 난수를 무작위로 하나 반환/ 양쪽 끝 값 모두 포함
import random
print(random.randint(1, 10))  #1~10 중 하나 출력
dice = random.randint(1,6)
print(f"주사위의 눈: {dice}")

#choice(): 시퀸스 자료형에서 무작위로 하나의 요소를 선택해서 반환
import random
menu = ['김밥', '라면', '떡볶이', '순대']
lunch = random.choice(menu)
print(f"오늘 점심은 {lunch}")

#shuffle(): 리스트의 요소를 무작위로 섞어, 직접 리스트를 바로 변경하는 함수
import random
cards = ['A', '2', '3', '4', '5']
random.shuffle(cards)
print("셔플된 카드:", cards)

#sample(): w중복 없이, 주어진 시퀀스에서 원하는 개수만큼 랜덤하게 선택해서 리스트로 반환
import random
lotto = random.samle(ranfe(1, 46), 6)
print("로또 번호:", lotto)

#random():0.0 이상 1.0미만의 실수 중에서 무작위 숫자 하나를 반환하는 함수
import random
value = random.random()
print("랜덤 실수:", value)

#uniform(a, b): a이상 b이하의 실수 중에서 무작위로 하나를 리턴하는 함수
import random
value = random.uniform(1.0, 10.0)
print("1~10 사이의 랜덤 실수:", value)

#triangular(): low 이상 high 이하의 실수 중에서, mode(가장 자주 나올 값)에 가까운 숫자를 무작위로 반환하는 함수
import random
num = random.triangular(1, 100, 70)
print("70 근처가 잘 나오는 랜덤 값:", round(num, 2))

#betavariate(alpha, beta):0.0부터 1.0 사이의 실수 중에서, 베타 분포를 따르는 무작위 값을 반환해
import random
value = random.betavariate(2.0, 5.0)
print(f"0~1 사이의 베타 분포 값: {value:.3f}")

#expovariate(lambd):지수 분포를 따르는 랜덤한 실수를 반환
import random
arrival_time = random.expovariate(1/5)
print(f"다음 고객 도착까지 대기시간: {round(arrival_time, 2)}분")

#gammavariate(alpha, beta): 지수 분포의 일반화/ 연속적인 사건의 누적 시간이나 총 대기 시간을 모델링할 때 사용
import random
alpha = 3
beta = 10
waiting_time = random.gammavariate(alpha, beta)
print(f"총 대기 시간 예상: {round(waiting_time, 2)}초")

#gauss(mu, sigma): 데이터가 평균값을 중심으로 종모양으로 퍼지는 확률분포
import random
height = random.gauss(170, 5)
print(f"생성된 키: {round(height, 2)}cm")

#lognormvariate(): 로그정규분포, 어떤 변수 x가 정규분포를 따른다면 y = exp(x)가 로그 정규 분포를 따른다고 보는 분포
import random
value = random.lognormvariate(0, 1)
print("생성된 로그 정규값:", round(value, 3))

#normalvariate(): 정규분포를 따르는 난수를 생성해. 종모양으로 자연현상에서 자주 나옴
import random
x = random.normalvariate(0, 1)
print("정규분포 난수:", round(x, 3))

#vonmisesvariate(mu, kappa): 원형 데이터에서 사용하는 난수 생성함수
import random
import math
angle = random.vonmisesvariate(0, 1)
print("생성된 각도(라디안):", round(angle, 3))
print("각도(도):", round(math.degrees(angle), 2))

#paretovariate(alpha): 파레토 분포를 따르는 난수를 생성하는 함수
import random
print("파레토 난수:", random.paretovariate(2.0))

#weibullvariate(alpha, beta):weibull 분포를 따르는 난수를 생성하는 함수
import random
result = random.weibullvariate(1.5, 500)
print("Weibull 난수:", round(result, 2))