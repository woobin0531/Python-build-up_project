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