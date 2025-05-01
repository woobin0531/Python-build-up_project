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

7
# 집합 만들기와 자료형 확인
# 아래 리스트를 집합(set)으로 변환하고, 그 자료형(type)을 출력하세요.
numbers = [1, 2, 2, 3, 4]
set_num = set(numbers)
print(type(set_num))

8
# 집합에서 요소 제거
# 아래 집합에서 'banana'를 제거한 뒤 결과를 출력하세요.
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)

9
# 집합의 포함 여부 확인
# 아래 집합에 숫자 7이 포함되어 있는지 True/False로 출력하세요.
s = {3, 5, 7, 9}
print(7 in s)