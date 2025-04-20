# "장보기" 프로그램을 함수로 변환하기
print("장보기를 시작합니다!")
items = ['사과', '바나나', '고구마', '양파', '토마토']

print("장바구니에 담을 항목은...")
for item in items:
    print(f"- {item}")

total_items = len(items)
print(f"총 {total_items}개의 물건을 구입할 예정입니다.")

print("구입이 완료되었습니다!")
# 풀이
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

# 간식 만들기
print("간식 만들기 시작!")

print("빵 꺼내기")
print("햄 꺼내기")
print("치즈 꺼내기")

print("빵에 햄 올리기")
print("그 위에 치즈 올리기")
print("빵 덮기")

print("완성된 간식 접시에 담기")
print("간식 만들기 끝!")

def snak_make(snak):
    print("간식 만들기 시작!")
def snack_준비():
    print("빵 꺼내기")
    print("햄 꺼내기")
    print("치즈 꺼내기")
def snack_순서():
    print("빵에 햄 올리기")
    print("그 위에 치즈 올리기")
    print("빵 덮기")
def finsh_snack():
    print("완성된 간식 접시에 담기")
def snack_실행setting():
    print("간식 만들기 시작!")
    snack_준비()
    snack_순서()
    finsh_snack()
    print("간식 만들기 끝!")
snack_실행setting()
#풀이
def 침대루틴():
    print("알람 끄기")
    print("기지개 켜기")
    print("세수하기")
    print("양치하기")

def 계란후라이():
    print("계란 후라이 만들기")
    print("밥 데우기")
    print("김 꺼내기")
    print("계란후라이 정식 완성!")

def 토스트():
    print("식빵 굽기")
    print("버터 바르기")
    print("딸기잼 바르기")
    print("토스트 완성!")

def 아침밥루틴(선택):
    print("냉장고에서 재료 꺼내기")
    if 선택 == "계란":
        계란후라이()
    elif 선택 == "토스트":
        토스트()
    else:
        print("해당 메뉴는 없습니다. 과일이라도 먹어요!")

def 나머지():
    print("옷 갈아입기")
    print("가방 챙기기")
    print("문 잠그고 나가기")

def 나가기준비():
    print("하루 시작!")
    침대루틴()
    menu = input("오늘 아침 뭐 먹을래? (계란 / 토스트): ")
    아침밥루틴(menu)
    나머지()

# 실행
나가기준비()

# 카페에서 주문 처리하기
def 손님응대():
  print("손님이 들어왔습니다.")
  print("메뉴를 보여줍니다.")
  print("손님이 아메리카노를 주문합니다.")

def 음료_제조():
  print("컵 준비하기")
  print("에스프레소 내리기")
  print("물 추가하기")
  print("아메리카노 완성!")
  print("손님에게 제공")

def 계산_및_마무리():
  print("결제 받기")
  print("손님 나감")

def main():
  손님응대()
  음료_제조()
  계산_및_마무리()

main()

# 영화관 예매 시스템
# 요구사항
"""사용자에게 영화 제목, 상영 시간, 예매 좌석 수를 입력 받는다.
사용자가 원하는 영화의 좌석이 남아 있는지 확인한 후 예매 여부를 결정한다.
예매가 가능한 경우, 예매한 좌석 수만큼 티켓을 출력해준다.
예매 불가한 경우 "좌석이 부족합니다!" 메시지를 출력한다."""
def 영화예매():
  영화제목 = input("영화제목을 입력하세요: ")
  상영시간 = input("상영시간을 입력하세요: ")
  좌석수 = int(input("예매 좌석 수를 입력하세요: "))
  return 영화제목, 상영시간, 좌석수

def 가능여부(영화제목, 상영시간, 좌석수):
  total_seats = 100
  가능한_좌석 = total_seats - 좌석수

  if 가능한_좌석 >= 0:
    print("예매 가능합니다")
    print(f"남은 좌석 {가능한_좌석}석")
  else:
    print("좌석이 부족합니다!")

def main():
  영화제목, 상영시간, 좌석수 =  영화예매()
  가능여부(영화제목, 상영시간, 좌석수)

main()
#풀이
# 예매를 여러 번 할 수 있음 (반복)
# 좌석 수가 예매될 때마다 줄어듦
# 좌석이 부족하면 예매 거절
# 예매 종료하고 싶으면 "q" 누르기

def 영화예매():
    영화제목 = input("영화 제목을 입력하세요 (종료: q): ")
    if 영화제목.lower == "q":
        return None, None, None

    상영시간 = input("상영시간을 입력해주세요: ")
    try:
        좌석수 = int(input("예매 좌석 수를 입력하세요: "))
    except valueError:
        print("숫자를 입력하세요")
        return None

    return 영화제목, 상영시간, 좌석수


def 가능여부(영화제목, 상영시간, 좌석수, 남은좌석):
    if 좌석수 <= 0:
        print("예매 수량은 1개 이상이어야 합니다.")
        return 남은좌석
    if 좌석수 <= 남은좌석:
        남은좌석 -= 좌석수
        print(f"{영화제목}({상영시간})예매 성공")
        print(f"남은 좌석: {남은좌석}석")
    else:
        print("좌석이 부족합니다")
    return 남은좌석


def main():
    총좌석 = 10
    남은좌석 = 총좌석
    print("영화예매 시스템 시작")

    while 남은좌석 > 0:
        영화제목, 상영시간, 좌석수 = 영화예매()

        if 영화제목 is None:
            print("예매를 종료합니다.")
            break

        남은좌석 = 가능여부(영화제목, 상영시간, 좌석수, 남은좌석)

    if 남은좌석 == 0:
        print("모든 좌석이 매진되었습니다")


main()

# 함수 구조화 + 조건 + 반복
def 카페_오픈():
  print("카페 오픈!")

def 손님응대():
  print("손님이 들어왔다")
  print("메뉴를 보여준다")
  menu = input("주문할 음료를 입력하세요 (아메리카노/카페라떼): ")
  return menu

def 음료제조(menu):
  print("컵 준비")
  print("에스프레소 내리기")
  if menu == "아메리카노":
    print("물 붓기")
  elif menu == "카페라떼":
    print("우유 붓기")
  else:
    print("해당 음료는 준비할 수 없습니다.")
    return
  print("손님에게 제공")

def 카페_마감():
  print("카페 마감!")

def main():
  카페_오픈()

  for i in range(3):
    print(f"{i+1}번째 손님 응대:")
    menu = 손님응대()
    음료제조(menu)

  카페_마감()
main()

# 치킨 주문 받기
요구사항
사용자에게 치킨 메뉴 이름과 수량을 입력받는다.
수량이 0보다 작거나 같으면 "잘못된 주문입니다"를 출력한다.
수량이 1개 이상이면 "주문하신 [치킨이름] [수량]개 준비 중입니다"를 출력한다.
def 주문받기():
  메뉴 = input("무슨 메뉴로 하시겠어요?: ")
  수량 = int(input("몇 인분을 시키겠어요?: "))
  return 메뉴, 수량

def 주문확인(메뉴, 수량):
  총_재고 = 5
  if 수량 <= 0:
    print(("잘못된 주문입니다"))
  elif 수량 > 총_재고:
    print(f"죄송합니다. {메뉴}는 현재 {총_재고}인분만 주문 가능합니다.")
  else:
    print(f"주문하신 {메뉴} {수량}게 준비 중입니다.")
    print("조리 시작...")
    for i in range(1, 수량 + 1):
      print(f"{i}번쩨 {메뉴} 준비 완료!")
    print("모든 주문 완료되었습니다")
def main():
  메뉴, 수량 = 주문받기()
  주문확인(메뉴, 수량)
main()


# 도서 대출 시스템

def 도서대출():
    사용자이름 = input("이름을 입력하세요:")
    도서제목 = input("대출할 책 제목을 입력하세요: ")
    return 사용자이름, 도서제목

def 남은_권수(사용자이름, 도서제목):
    남은권수 = 3
    if 남은권수 > 0:
        print(f"{사용자이름}님께 {도서제목}책을 대출합니다.")
        남은권수 -= 1
        print(f"남은 책 수: {남은권수}")
    else:
        print("다출 가능한 책이 없습니다")

def main():
    print("도서 대출 시스템입니다.")
    사용자이름, 도서제목 = 도서대출()
    남은_권수(사용자이름, 도서제목)
main()
#풀이
def 사용자정보입력():
  이름 = input("이름을 입력하세요")
  책제목 = input("대출할 책 제목을 입력하세요: ")
  return 이름, 책제목

def 대출가능여부확인(남은권수):
  return 남은권수 > 0

def 책대출(이름, 책제목, 남은권수):
  if 대출가능여부확인(남은권수):
    print(f"{이름}님께서{책제목} 책을 대출합니다. ")
    남은권수 -= 1
    print(f"남은 책 수: {남은권수}권")
  else:
    print("대출 가능한 책이 없습니다")
  return 남은권수

def main():
  print("도서 대출 시스템입니다.")
  남은권수 = 3
  이름, 책제목 = 사용자정보입력()
  남은권수 = 책대출(이름, 책제목, 남은권수)

main()

# 패스트푸드 키오스크 시스템
요구사항
손님에게 이름을 입력받는다.
메뉴(햄버거, 감자튀김, 콜라) 중 원하는 것을 고르게 한다.
각 메뉴의 가격은 다음과 같다:
햄버거: 5000원
감자튀김: 2000원
콜라: 1500원
수량을 입력받고, 총 가격을 계산해서 출력한다.
0 이하의 수량을 입력하면 "잘못된 주문입니다" 출력 후 종료한다.
def 주문받기():
  menu = input("메뉴를 선택해주세여(햄버거/감자튀김/콜라): ")
  수량 = int(input("수량을 입력하세요: "))
  return menu, 수량

def 주문(menu, 수량):
  메뉴 = [(햄버거, 5000), (감자튀김, 2000), (콜라, 1500)]
  햄버거_재고 = 5
  감자튀김_재고 = 4
  콜라_재고 = 3
  #햄버거만들기
  for menu, 수량 in 메뉴.items[0]:
    if 수량 > 햄버거_재고:
      print("재고가 없습니다.")
    elif 수량 <= 햄버거_재고:
      print(f"{메뉴}를 {수량}개 만드는 중")
      헴버거_재고 -= 수량
    else:
      print("그런 메뉴는 없습니다.")
  #감자튀김만들기
  for menu, 수량 in 메뉴, items[1]:
    if 수량 > 감자튀김_재고:
      print("재고가 없습니다.")
    elif 수량 <= 감자튀김_재고:
      print(f"{메뉴}를 {수량}개 만드는 중")
    else:
      print("그런 메뉴는 없습니다.")
  #콜라만들기
  for menu, 수량 in 메뉴, items[2]:
    if 수량 > 콜라_재고:
      print("재고가 없습니다.")
    elif 수량 <= 콜라_재고:
      print(f"{메뉴}를 {수량}개 만드는 중")
    else:
      print("그런 메뉴는 없습니다.")

def 총_가격():
  for menu, 수량 in 메뉴.items():
    for i in range(수량):
      수량 * 재고 - (감자, 햄버거, 콜라)

#풀이
menu_list = [("햄버거", 5000), ("감자튀김", 2000), ("콜라", 1500)]
stock_list = [5, 4, 3]

def 주문받기():
  menu = input("메뉴를 선택해주세요 (햄버거/감자튀김/콜라): ")
  수량 = int(input("수량을 입력해주세요: "))
  return menu, 수량

def 주문처리(menu, 수량):
  found = False  #found 초기화
  for i in range(len(menu_list)):
    이름, 가격 = menu_list[i]
    if 이름 == menu:
      found = True
      if 수량 <= 0:
        print("잘못된 수량입니다.")
        return
      if stock_list[i] < 수량:
        print(f"재고가 부족합니다. 남은 재고: {stock_list[i]}개")
      #주문성공
      print(f"{이름} {수량}개 만드는 중")
      stock_list[i] -= 수량
      총가격 = 가격 * 수량
      print(f"총 가격은 {총가격}원입니다")
      print(f"{이름}남은 재고:{stock_list[i]}개")
      return
  if not found:
    print("해당 메뉴는 없습니다.")

def main():
  print("패스트푸드 키오스크입니다")
  menu, 수량 = 주문받기()
  주문처리(menu, 수량)

main()

# 가상 도서관 관리 시스템
# 요구사항
도서 대출: 사용자가 이름과 원하는 책 제목을 입력하여 책을 대출합니다. (책 제목은 미리 설정된 책 목록에서만 선택 가능)
도서 반납: 사용자가 대출한 책을 반납할 때, 반납한 책을 목록에서 제거합니다.
대출 가능한 책 목록과 현재 대출 중인 책 목록을 출력하는 기능을 포함해야 합니다.
대출할 수 있는 책 수는 최대 5권으로 제한합니다.
# 조건:
대출할 수 있는 책 목록은 "책1", "책2", "책3", "책4", "책5"로 설정해 주세요.
반납할 책을 선택하고, 그 책을 다시 대출 목록에 추가합니다.
대출 시 책 제목과 수량을 입력받고, 반납 시 책 제목을 입력받습니다.
대출된 책 목록을 확인할 수 있는 기능도 필요합니다.
#풀이
def 도서_출력(도서_목록, 대출중_목록):
  print("현재 대출 가능한 책 목록: ")
  for 책 in 도서_목록:
    print(책)
  print("대출중인 책목록: ")
  for 책 in 대출중_목록:
    print(책)

def 도서_대출(도서_목록, 대출중_목록):
  사용자이름 = input("이름을 입력하세요: ")
  책제목 = input("대출할 책 제목을 입력하세요: ")

  if 책제목 in 도서_목록:
    if len(대출중_목록) < 5:
      도서_목록.remove(책제목)
      대출중_목록.append(책제목)
      print(f"{사용자이름}님, {책제목} 책을 대출하셨습니다.")
    else:
      print("대출 가능한 최대 권수를 초과했습니다. 반납 후 대출 가능합니다.")
  else:
    print("선택한 책은 대출할 수 없습니다. 목록을 확인해주세요.")

def 도서_반납(도서_목록, 대출중_목록):
  사용자이름 = input("이름을 입력하세요: ")
  책제목 = input("반납할 책 제목을 입력하세요: ")
  if 책제목 in 대출중_목록:
    대출중_목록.remove(책제목)
    도서_목록.append(책제목)
    print(f"{사용자이름}님, {책제목} 책을 반납하셨습니다.")
  else:
    print("대출 중인 책 목록에 해당 책이 없습니다.")

def main():
  도서_목록 = ["책1", "책2", "책3", "책4", "책5"]
  대출중_목록 = []

  while True:
    print("1 도서 목록 확인")
    print("2 도서 대출")
    print("3 도서 반납")
    print("4 종료")
    선택 = input("원하는 작업을 선택하세요")

    if 선택 == "1":
      도서_출력(도서_목록, 대출중_목록)
    elif 선택 == "2":
      도서_대출(도서_목록, 대출중_목록)
    elif 선택 == "3":
      도서_반납(도서_목록, 대출중_목록)
    elif 선택 == "4":
        print("시스템을 종료합니다.")
        break
    else:
      print("잘못된 선택입니다. 다시 시도하세요.")
main()

