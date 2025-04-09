#다음 튜플에서 숫자 2가 몇 번 나오는지 구하세요
numbers = (1, 2, 3, 2, 4, 2, 5)
numbers.count(2)

#다음 튜플에서 값 7의 첫 번째 위치(index) 를 구하세요.
nums = (3, 5, 7, 9, 7, 11)
nums.index(7)

# 각 학생의 이름과 점수를 출력해 보세요.
students = [("우빈", 90), ("지민", 85), ("하늘", 92)]
for name, score in students:
  print(f"{name}의 점수는 {score}입니다")

#리스트에서 중복을 제거한 후, 집합(set)으로 출력하세요.
nums = [1, 2, 3, 2, 4, 3, 5, 1]
a = set(nums)
print(a)

#중복된 과일을 제거하고, 오름차순으로 정렬된 리스트를 출력하세요.
fruits = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
unique_fruits = set(fruits)
sorted(unique_fruits)

#학생 A와 B가 듣는 과목이 있을 때, 두 학생이 공통으로 듣는 과목을 출력하세요.
student_a = {"국어", "영어", "수학"}
student_b = {"수학", "과학", "영어"}
c = student_a & student_b

#아래 두 집합이 공통 요소가 없는지 확인하고, 결과를 출력하세요
x = {"a", "b", "c"}
y = {"d", "e", "f"}
result = x.isdisjoint(y)
print("공통 원소 없음:", result)

#파티룸 예약 시스템에서 사용자들이 예약 요청을 했는데,
#중복 예약자가 생겼다고 해!
#중복으로 예약한 사람을 찾아서 출력해줘.
from collections import Counter
day1 = {"우빈", "지민", "수민", "하늘", "민수"}
day2 = {"하늘", "지민", "나영", "수민", "정우"}
day3 = {"지민", "민수", "정우", "수민"}
total = day1 | day2 | day3  # total = day1.union(day2,day3)
counter = Counter()
for day in [day1, day2, day3]:
  for name in  day:
    counter[name] += 1
duplicate = [name for name, count in counter.items() if count >=2]
print(duplicate)

#0부터 4까지 제곱한 리스트 만들기
squares = [x**2 for x in range(5)]

#짝수만 뽑기
evens = [x for x in range(10) if x % 2 ==0]
print(evens)

#value가 90 이상인 학생들만
scores = {"우빈": 92, "지민": 88, "수민": 95}
max_score = [name for name, score in scores.items() if score >=90]
print(max_score)