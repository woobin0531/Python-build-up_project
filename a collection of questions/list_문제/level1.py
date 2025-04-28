1
# 리스트의 길이 출력하기
# 아래 리스트에 들어있는 요소의 개수를 출력하세요.
colors = ["red", "blue", "green", "yellow", "pink"]
print(len(colors))

2
# 리스트의 마지막 요소 출력하기
# 아래 리스트의 마지막 값을 출력하세요.
numbers = [11, 22, 33, 44, 55]
print(numbers[-1])

3
# 특정 값 세기
# 주어진 리스트에서 숫자 3이 몇 번 나오는지 출력하세요.
numbers = [1, 3, 5, 3, 7, 3, 9]
# 출력 예시: 3
print(numbers.count(3))

4
# 리스트 뒤집기
# 주어진 리스트를 뒤집어서 출력하세요.
fruits = ["apple", "banana", "cherry"]
# 출력 예시: ['cherry', 'banana', 'apple']
print(fruits[::-1])

5
# 모든 요소 더하기
# 아래 리스트에 있는 모든 숫자의 합을 구하세요.
scores = [85, 90, 78, 92, 88]
# 출력 예시: 433
print(sum(scores))

6
# 리스트 요소의 합 구하기
# 주어진 리스트 [10, 20, 30, 40]의 모든 요소를 더한 결과를 출력하세요.
a = [10, 20, 30, 40]
print(sum(a))

7
# 리스트에서 특정 값 개수 세기
# 리스트 ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']에서
# 'apple'이 몇 번 나오는지 세어 출력하세요.
a = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
b = a.count('apple')
print(b)