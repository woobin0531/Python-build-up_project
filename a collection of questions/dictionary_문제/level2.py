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