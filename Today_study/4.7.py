# 'age' 값을 출력하세요.
student = {"name": "우빈", "age": 20, "grade": "A"}
print(student['age'])

# 'english': 95를 추가한 딕셔너리를 출력하세요.
score = {"math": 90, "science": 85}
score1 = {'english': 95}
score.update(score1)
print(score)

#다음 딕셔너리에서 모든 키만 출력해보세요.
fruits = {"apple": 1200, "banana": 800, "orange": 1000}
a = fruits.keys()
print(a)

#사용자가 찾고 싶은 과일 이름을 입력하면, 딕셔너리에 그 과일이 있는지 출력하세요.
#딕셔너리에 있으면 "있어요!", 없으면 "없어요!"라고 출력합니다.
a = input("과일을 입력하세요: ")
fruits = {"apple": 1200, "banana": 800, "orange": 1000}
if a in fruits:
    print("있어요")
else:
    print("없어요")

#다음 딕셔너리에서 가격의 총합을 구해보세요.
menu = {"떡볶이": 3000, "김밥": 2500, "순대": 3500}
s = menu.values()
sum(s)

# 빈 딕셔너리를 만들고 이름과 나이를 입력받아 추가해보세요.
# 예: {"우빈": 25}
people = {}
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
# 여기에 추가하는 코드 작성
people[name] = age
print(people)

info = {"이름": "우빈", "나이": 25, "직업": "개발자"}
# 아래처럼 출력되게 만들어보세요
# 이름: 우빈
# 나이: 25
# 직업: 개발자
# 여기에 코드 작성
for key, value in info.items():
  print(f'{key}: {value}')

stock = {"사과": 10, "바나나": 5, "귤": 8}
# 바나나 재고를 10개로 변경하세요.
# 결과: {'사과': 10, '바나나': 10, '귤': 8}
# 여기에 코드 작성
stock['바나나'] = 10
print(stock)

#다음은 가게에서 판매 중인 물건들의 재고 수량을 딕셔너리로 표현한 것이다.
#재고가 5개 이상인 물건의 이름만 출력하시오.
stock = {"사과": 3, "바나나": 7, "귤": 5, "키위": 2}
for item, quantity in stock.items():
  if quantity >= 5:
    print(item)

#다음은 물건 이름과 가격을 저장한 딕셔너리다.
#가장 비싼 물건의 이름과 가격을 출력하시오.
items = {"노트북": 1000000, "모니터": 300000, "마우스": 15000, "키보드": 50000}
max_price = -1
max_item = ""
for item in items:
  if items[item] > max_price:
    max_price = items[item]
    max_item = item
print("가장 비싼 제품: ",  max_item)
print("가격: ", max_price)
'''
most_expensive = max(items.items(), key=lambda x:x[1])
print("가장 비싼제품:", mosot_expensive[0])
print("가격:", most_expensive[1])
'''

#다음은 학생 이름과 세 과목의 점수를 저장한 딕셔너리다.
#각 학생의 이름과 평균 점수를 함께 출력하시오.
scores = {
    "우빈": [80, 90, 100],
    "지수": [70, 85, 95],
    "현우": [88, 64, 72]
}
for student, score in scores.items():
  avg = sum(score)/len(score)
  print(f"{student}의 평균 점수는 {avg:.1f}점 입니다.")

#다음 딕셔너리에서 가장 저렴한 물건의 이름을 출력하세요.
items = {
    "책상": 120000,
    "의자": 45000,
    "노트북 거치대": 20000,
    "모니터암": 38000
}
min_items = ""
min_price = float('inf')
for item in items:
  if items[item] < min_price:
    min_price = items[item]
    min_item = item
print(min_item)
print(min_price)
'''
cheapest_item = min(items, key=items.get)
print(cheapest_item)
'''

#다음 제품별 판매 수량 딕셔너리에서 가장 많이 팔린 제품명을 출력하세요.
sales = {
    "커피": 310,
    "녹차": 150,
    "에너지드링크": 520,
    "물": 400
}
hot_sales = -1
sale1 = ""
for sale in sales:
  if sales[sale] > hot_sales:
    hot_sales = sales[sale]
    sale1 = sale
print(sale1)
print(hot_sales)

#학생별 시험 점수가 담긴 딕셔너리가 있습니다.
#가장 높은 점수를 받은 학생의 이름과 점수를 함께 출력하세요
scores = {
    "우빈": 88,
    "지수": 95,
    "민재": 90,
    "서윤": 99,
    "현우": 85
}
top_student = max(scores, key=scores.get)   # key=scores.get 형식 지켜줘야 함
print(top_student, scores[top_student])

#점수 90점 이상인 과목만 출력하기
scores = {"국어": 92, "수학": 88, "영어": 95, "과학": 91}
for subject, score in scores.items():
  if score >= 90:
    print(subject)
scores = {"국어": 92, "수학": 88, "영어": 95, "과학": 91}
max_subject = ""
max_score = -1  # 초기값 작게 설정

for subject, score in scores.items():
    if score > max_score:
        max_score = score
        max_subject = subject
print(max_subject, max_score)

#가장 높은 점수의 과목과 점수 출력하기
scores = {"국어": 92, "수학": 88, "영어": 95, "과학": 91}
max_score = -1
max_subject = ""
for subject, score in scores.items():
  if score > max_score:
    max_score = score
    max_subject = subject
print(max_subject, max_score)

#딕셔너리에서 값이 짝수인 키만 출력하기
nums = {"a": 1, "b": 2, "c": 3, "d": 4}
for key, value in nums.items():
  if value % 2 == 0:
    print(key)

#사용자에게 키를 입력받아 해당하는 값을 출력하되, 키가 없으면 "존재하지 않음" 출력하기
key = input("키를 입력하세요: ")
fruits = {"apple": 1000, "banana": 800, "melon": 1500}
print(fruits.get(key, "존재하지 않음"))

#값이 가장 낮은 항목의 키 출력하기
scores = {"math": 70, "science": 85, "english": 65, "history": 90}
lowest_key = min(scores, key=scores.get)
print(lowest_key)