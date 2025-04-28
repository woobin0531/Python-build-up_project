# 딕셔너리 값 출력하기
# 아래 딕셔너리에서 이름을 출력하세요.
person = {"name": "Alice", "age": 25, "city": "Seoul"}
print(person["name"])

# 딕셔너리에 항목 추가하기
# 아래 딕셔너리에 키 "job"과 값 "developer"를 추가하세요.
info = {"name": "Bob", "age": 30}
info["job"] = "developer"
print(info)

# 딕셔너리 키 목록 출력하기
# 아래 딕셔너리에서 모든 키를 리스트로 만들어 출력하세요.
student = {"id": 101, "name": "Eunji", "grade": "A"}
keys = list(student.keys())
print(keys)

# 값 기준으로 조건 출력하기
# 점수가 80점 이상인 학생들만 출력하세요.
scores = {"Anna": 82, "Ben": 77, "Clara": 91, "David": 65}
for key, value in scores.items():
  if value >= 80:
    print(key)

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

# 값 변경하기
# 아래 딕셔너리에서 "age" 값을 40으로 변경하세요.
person = {"name": "Charlie", "age": 28, "city": "Busan"}
person["age"] = 40
print(person)

# 딕셔너리 병합하기
# 아래 두 개의 딕셔너리를 병합해서 하나의 딕셔너리를 만들고 출력하세요.
# 단, 키가 겹칠 경우 두 값을 더해서 저장하세요.
dict1 = {"a": 3, "b": 5, "c": 1}
dict2 = {"b": 2, "c": 4, "d": 6}
dict3 = {}
for key in dict1:
  dict3[key] = dict1[key]
for key in dict2:
  if key in dict3:
    dict3[key] += dict2[key]
  else:
    dict3[key] = dict2[key]
print(dict3)

# 가장 많은 등장 횟수
# 문자열이 주어졌을 때, 각 문자별 등장 횟수를 세고
# 가장 많이 등장한 문자를 출력하세요.
# 예: "mississippi" → "i"
test = "mississippi"
count_test = {}
for i in test:
  if i in count_test:
    count_test[i] += 1
  else:
    count_test[i] = 1

max_count = 0
max_i = ""
for key in count_test:
  if count_test[key] > max_count:
    max_count = count_test[key]
    max_i = key
print(max_i)

# 값으로 정렬된 딕셔너리 만들기
# 아래 딕셔너리를 값 기준 내림차순으로 정렬해서
# 새로운 딕셔너리로 출력하세요.
scores = {"Alice": 82, "Bob": 95, "Charlie": 78, "David": 90}
sorted_scores = sorted(scores.items(), key = lambda x: x[1], reverse=True)
print(sorted_scores)

# 다음과 같은 딕셔너리에서 이름(key)과 점수(value)를 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for i in scores:
  print(f"{i}: {scores[i]}")

# 다음 딕셔너리에 "David": 88을 추가하고, 전체를 출력하세요.
scores = {"Alice": 85, "Bob": 92}
scores["David"] = 88
print(scores)

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

# 점수 평균 내기
# 아래와 같은 딕셔너리가 있을 때, 전체 사람의 평균 점수를 구해서 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
scores2 = 0
for i in scores.values():
  scores2 += i
avr = scores2 / len(scores)
print(f"평균은 {avr}입니다.")

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

# 두 딕셔너리 병합
# 문제: 두 개의 딕셔너리를 병합해서 하나의 딕셔너리로 만드세요.
# 중복 키가 있을 경우 두 번째 딕셔너리의 값을 사용합니다.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = dict1.copy()
result.update(dict2)
print(result)

# 학생별 평균 점수 구하기
# 문제: 다음과 같이 학생별로 과목 점수가 저장된 딕셔너리가 있습니다.
# 각 학생의 평균 점수를 구해 새로운 딕셔너리로 만드세요.
scores = {
    "Alice": {"math": 90, "english": 85, "science": 88},
    "Bob": {"math": 72, "english": 78, "science": 80},
    "Charlie": {"math": 95, "english": 100, "science": 98}
}
avr_scores = {}

for name, value in scores.items():
  scores_a = 0
  for subject, score in value.items():
    scores_a += score
  avr = round(scores_a / len(value), 2)
  avr_scores[name] = avr
print(avr_scores)

scores = {
    "Alice": {"math": 90, "english": 85, "science": 88},
    "Bob": {"math": 72, "english": 78, "science": 80},
    "Charlie": {"math": 95, "english": 100, "science": 98}
}

avr_scores = {}

for name, subjects in scores.items():
    total = 0
    for subject, score in subjects.items():
        total += score
    average = round(total / len(subjects), 2)
    avr_scores[name] = average

print(avr_scores)
