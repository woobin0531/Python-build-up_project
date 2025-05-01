1
# 딕셔너리 값 출력하기
# 아래 딕셔너리에서 이름을 출력하세요.
person = {"name": "Alice", "age": 25, "city": "Seoul"}
print(person["name"])

2
# 딕셔너리에 항목 추가하기
# 아래 딕셔너리에 키 "job"과 값 "developer"를 추가하세요.
info = {"name": "Bob", "age": 30}
info["job"] = "developer"
print(info)

3
# 딕셔너리 키 목록 출력하기
# 아래 딕셔너리에서 모든 키를 리스트로 만들어 출력하세요.
student = {"id": 101, "name": "Eunji", "grade": "A"}
keys = list(student.keys())
print(keys)

4
# 값 변경하기
# 아래 딕셔너리에서 "age" 값을 40으로 변경하세요.
person = {"name": "Charlie", "age": 28, "city": "Busan"}
person["age"] = 40
print(person)

5
# 다음과 같은 딕셔너리에서 이름(key)과 점수(value)를 출력하세요.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for i in scores:
  print(f"{i}: {scores[i]}")

6
# 다음 딕셔너리에 "David": 88을 추가하고, 전체를 출력하세요.
scores = {"Alice": 85, "Bob": 92}
scores["David"] = 88
print(scores)

7
# 딕셔너리 키 리스트 만들기
# 아래 딕셔너리에서 모든 키(key)만 리스트로 만들어 출력하세요
fruit_prices = {"apple": 1000, "banana": 800, "orange": 1200}
print(list(fruit_prices.keys()))

8
# 딕셔너리 값 변경
# 아래 딕셔너리에서 "math" 과목의 점수를 95로 변경하세요.
scores = {"math": 80, "english": 90, "science": 85}
scores["math"] = 95
print(scores)

9
# 딕셔너리 항목 삭제
# 아래 딕셔너리에서 "cat" 항목을 삭제하세요.
animals = {"dog": "강아지", "cat": "고양이", "bird": "새"}
animals.pop("cat")
print(animals)