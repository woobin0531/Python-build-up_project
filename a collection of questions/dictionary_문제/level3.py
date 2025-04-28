1
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

2
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

3
# 값으로 정렬된 딕셔너리 만들기
# 아래 딕셔너리를 값 기준 내림차순으로 정렬해서
# 새로운 딕셔너리로 출력하세요.
scores = {"Alice": 82, "Bob": 95, "Charlie": 78, "David": 90}
sorted_scores = sorted(scores.items(), key = lambda x: x[1], reverse=True)
print(sorted_scores)

4
# 두 딕셔너리 병합
# 문제: 두 개의 딕셔너리를 병합해서 하나의 딕셔너리로 만드세요.
# 중복 키가 있을 경우 두 번째 딕셔너리의 값을 사용합니다.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = dict1.copy()
result.update(dict2)
print(result)

5
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

'''
avr_scores = {}

for name, subjects in scores.items():
    total = 0
    for subject, score in subjects.items():
        total += score
    average = round(total / len(subjects), 2)
    avr_scores[name] = average

print(avr_scores)'''