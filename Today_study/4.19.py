# 커피 머신 자동화
def make_coffee(cup_count):
  if cup_count <= 0:
      print("커피 주문이 없습니다")
      return
  print("커피머신 예열 중")

  for i in range(1, cup_count + 1):
    print(f"{i}번째 커피 만드는 중..")

  print("모든 커피 완성!")
  return f"총 {cup_count}잔 커피가 완성되었습니다"
result = make_coffee(0)
print(result)

# 오므라이스 자동 조리기
def make_omurice(plate_count):
  if plate_count <= 0:
    print("재료가 부족합니다! 조리를 취소합니다")
    return
  print("프라이팬 예열 중")
  for i in range(1, plate_count + 1):
    print(f"{i}번째 오므라이스 만드는 중...")
  print("모든 오므라이스 완성")
  return f"총 {plate_count}그릇의 오므라이스가 완성되었습니다!"
result = make_omurice(3)
print(result)

# 주문형 요리 자동 조리기
def cook_order(name, menu, count):
  if count <= 0:
    print("주문 수량이 0개 이하입니다. 주문을 취소합니다.")
    return

  print(f"{name}님의 {menu} {count}개 주문 접수!")
  print(f"조리시작: {menu} 만드는 중...")
  print()

  for i in range(1, count+1):
    print(f"{i}번째 {menu} 조리중..")
  print(f"{menu} {count}개 완성!")

result = cook_order("우빈", "커피", 3)
print(result)

# 초간단 계산기
def push_push():
  x = int(input("첫 번째 숫자를 입력하세요: "))
  y = int(input("두 번째 숫자를 입력하세요: "))
  return x, y

def calculate(x, y):
  print("덧셈 결과:", x + y)
  print("뺄셈 결과:", x - y)
  print("곱셈 결과:", x * y)
  if y != 0:
    print("나눗셈 결과:", x / y)
  else:
    print("0으로 나눌 수 없습니다.")

def run_calculator():
  print("간단한 계산기입니다.")
  x, y = push_push()
  calculate(x, y)

run_calculator()

# 김밥 만들기 자동화 함수 만들기
# 조건:손님 이름과 김밥 개수를 받아서
# 김밥을 하나씩 만드는 과정을 출력하고
# 마지막에 완료 메시지를 리턴

def kimbab_make(name, count):
  if count <= 0:
    print("주문을 취소합니다.")
    return "조리 실패"
  print()
  print(f"{name}님의 김밥을 만들기 시작합니다")
  print(f"{count}개 주문이 들어왔습니다")

  for i in range(1, count+1):
        print(f"{i}번째 김밥: 김 올리기")
        print(f"{i}번째 김밥: 밥 얹기")
        print(f"{i}번째 김밥: 재료 넣기")
        print(f"{i}번째 김밥: 말기\n")
  return f"총 {count}줄 김밥 완성! 감사합니다 {name}님"

result = kimbab_make("우빈", 2)
print(result)

# "장보기" 프로그램을 함수로 변환하기
print("장보기를 시작합니다!")
items = ['사과', '바나나', '고구마', '양파', '토마토']

print("장바구니에 담을 항목은...")
for item in items:
    print(f"- {item}")

total_items = len(items)
print(f"총 {total_items}개의 물건을 구입할 예정입니다.")

print("구입이 완료되었습니다!")
def show_shopping_list(items):
  print("장바구니에 담을 항목은...")
  for item in items:
    print(f"- {item}")

def count_items(items):
  total_items = len(items)
  print(f"총 {total_items}개의 물건을 구입할 예정입니다.")
  return total_items

def start_shopping():
  print("장보기를 시작합니다")
  items = ["사과", "바나나", "고구마", "양파", "토마토"]

  show_shopping_list(items)
  count_items(items)

  print("구입이 완료되었습니다!")

start_shopping()

# 실제 계산 가능한 장보기 프로그램 만들기
# 목표: 사용자가 직접 물건 이름과 가격을 입력
# 입력은 여러 번 받고, '끝'이라고 치면 입력 종료
# 모든 항목을 출력하고
# 총 가격을 계산해서 출력
def input_items():
  items = []
  print("장보기 시작!")

  while True:
    name = input("물건 이름을 입력하세요 (끝내려면 '끝' 입력): ")
    if name == "끝":
      break
    try:
      price = int(input(f"{name}의 가격을 입력하세요:"))
      items.append((name, price))
    except valueerror:
      print("가격은 숫자로 입력해야 해요. 다시 시도해 주세요")

  return items

def show_items(items):
  print("[장바구니 목록]")
  for name, price in items:
    print(f"-{name}: {price}원")

def calculate_total(items):
  total = sum(price for _, price in items)
  print(f"총 가격은 {total}원 입니다.")

def start_shopping():
  items = input_items()
  if items:
    show_items(items)
    calculate_total(items)
  else:
    print("아무것도 장바구니에 담지 않았습니다.")
start_shopping()