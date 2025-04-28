1
# 튜플에서 홀수만 추출하기
numbers = (1, 2, 3, 4, 5, 6, 7)
# 출력 예시: (1, 3, 5, 7)
print(numbers[0::2])

2
# 튜플의 최대값과 최소값 출력하기
data = (10, 25, 7, 50, 34)
# 출력 예시: max: 50, min: 7
a = max(data)
b = min(data)
print("max:",a ,"min:", b)

3
# 튜플에서 문자열의 길이 출력하기
words = ("apple", "banana", "kiwi")
# 출력 예시: 5 6 4
for i in words:
  print(len(i), end=" ")

4
# 튜플에서 합계 구하기
# 주어진 튜플의 모든 숫자를 더한 값을 출력하세요.
numbers = (1, 2, 3, 4, 5)
# 출력 예시: 15
print(sum(numbers))

5
# 특정 값 개수 세기
# 주어진 튜플에서 숫자 2가 몇 번 나오는지 세어 출력하세요.
numbers = (1, 2, 3, 2, 4, 2, 5)
# 출력 예시: 3
numbers.count(2)

6
# 튜플에서 특정 값의 개수 세기
# 설명: 주어진 튜플에서 숫자 7이 몇 번 등장하는지 세어 출력하세요.
nums = (7, 3, 5, 7, 8, 7, 2)
# 출력 예시: 3
nums.count(7)