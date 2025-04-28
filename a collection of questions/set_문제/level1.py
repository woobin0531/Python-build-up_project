1
# 중복 제거하기
# 리스트에서 중복된 항목을 제거하고, set으로 출력하세요
items = ["apple", "banana", "apple", "orange", "banana", "grape"]
# 출력 예: {'apple', 'banana', 'orange', 'grape'}
print(set(items))

2
# 두 집합의 공통 요소 찾기
# 두 집합에서 공통으로 들어있는 요소만 출력하세요.
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}
# 출력 예: {'banana', 'cherry'}
print(set1&set2)

3
# 집합 차집합 구하기
# 다음 두 집합에서 set1에는 있고 set2에는 없는 요소들을 출력하세요.
set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e"}
# 출력 예: {'a', 'b'}
print(set1-set2)

4
# 중복 제거하기
# 리스트에 있는 중복 숫자를 제거하고 집합(set)으로 출력하세요.
numbers = [1, 2, 2, 3, 4, 4, 5]
# 출력 예시: {1, 2, 3, 4, 5}
set(numbers)

5
# 두 집합의 교집합 구하기
# 아래 두 집합에서 공통으로 존재하는 숫자만 출력하세요.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 출력 예시: {3, 4}
print(a&b)

6
# 차집합 구하기
# a 집합에만 있고, b 집합에는 없는 요소만 출력하세요.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 출력 예시: {1, 2}
print(a-b)