#설명
#김, 고, 장, 백은 모임에서 식당과 바를 갔다가 카페를 갔다.
#이 때 식당, 바, 카페에서 나온 금액을 각각 입력받고 각자 먹은 만큼 계산할 수 있는 코드를 만든다.
#각각의 인원은 중간까지만 가거나, 중간에 합류할 수 있다.
#예시)고와 장은 식당은 가지 않고 바에서 합류했으며, 백과 장은 카페를 가지 않고 먼저 일어났다.

def 식당():
  a = int(input("금액: "))
  식당조합 = ["김_pay", "백_pay"]
  for i in 식당조합:
    i = a / len(식당조합)

def 바():
  b = int(input("금액: "))
  바조합 = ["김_pay", "고_pay", "장_pay". "백_pay"]
  for ii in 바조합:
    ii = b / len(바조합)
#김 고 장 백

#카페
c = int(input("금액: "))
카페조합 = ["김_pay", "고_pay"]
for iii in 카페조합:
  iii c / len(카페조합)
#김 고
-----------
pay = {"김": 0, "고": 0, "장": 0, "백": 0}

def 식당():
  a = int(input("식당 금액 입력: "))
  참석자 = ["김", "백"]
  per_person = a / len(참석자)
  for name in 참석자:
    pay[name] += per_person

def 바():
  a = int(input("바 금액 입력: "))
  참석자 = ["김", "고", "장", "백"]
  per_person = a / len(참석자)
  for name in 참석자:
    pay[name] += per_person

def 카페():
  a = int(input("카페 금액 입력: "))
  참석자 = ["김", "고"]
  per_person = a / len(참석자)
  for name in 참석자:
    pay[name] += per_person

def main():
  식당()
  바()
  카페()
  for name, amount, in pay.items():
    print(f"{name}: {amount}원")

main()