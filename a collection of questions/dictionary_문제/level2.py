1
# 값 기준으로 조건 출력하기
# 점수가 80점 이상인 학생들만 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
for key, value in scores.items():
  if value >= 80:
    print(key)

2
# 가장 높은 점수를 받은 학생 찾기
# 아래 딕셔너리에서 최고 점수를 받은 학생의 이름을 출력하세요.
grades = {"John": 85, "Lisa": 92, "Tom": 88, "Nina": 90}
best = max(grades.values())
for name, score in grades.items():
  if score == best:
    print(name)
"""best_score = -1
best_student = ""
for name, score in grades.items():
  if score > best_score:
    best_score = score
    best_student = name
print(best_student)"""

3
# 다음 딕셔너리에서 value 값이 90 이상인 사람만 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
for name, score in scores.items():
  if scores[name] >= 90:
    print(f"90점 이상인사람은 {name}입니다")

"""
for name in scores:
    if scores[name] >= 90:
        print(name, scores[name])
"""

4
# 점수 평균 내기
# 아래와 같은 딕셔너리가 있을 때, 전체 사람의 평균 점수를 구해서 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
scores2 = 0
for i in scores.values():
  scores2 += i
avr = scores2 / len(scores)
print(f"평균은 {avr}입니다.")

5
# 최고 점수 받은 사람 찾기
# 문제: 가장 점수가 높은 사람의 이름과 점수를 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
most_score = -1
most_name = ""
for name, score in scores.items():
  if score > most_score:
    most_score = score
    most_name = name
print(f"{most_score}점인 {most_name}입니다")

6
# 두 개의 리스트를 딕셔너리로 변환
# 아래 두 개의 리스트를 이용해, 과일 이름을 키로, 가격을 값으로 하는 딕셔너리를 생성하세요.
fruits = ["apple", "banana", "peach"]
prices = [3000, 2000, 4000]
fruit_dict = dict(zip(fruits, prices))
print(fruit_dict)

7
# 딕셔너리에서 값 기준으로 키 찾기
# 아래 딕셔너리에서 값이 1인 모든 키를 리스트로 만들어 출력하세요.
word_count = {'big': 1, 'good': 1, 'sky': 1, 'blue': 0, 'mouse': 1}
list_word = []
for word, count in word_count.items():
  if count == 1:
    list_word.append(word)
print(list_word)

8
# 딕셔너리 컴프리헨션 활용
# 1부터 5까지의 수를 키로 하고,각 키의 제곱을 값으로 하는 딕셔너리를
# 딕셔너리 컴프리헨션으로 한 줄에 만드세요
dict_a = {x: x**2 for x in range(1, 6)}
print(dict_a)