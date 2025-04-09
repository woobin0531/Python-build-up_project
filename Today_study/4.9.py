#2단부터 9단까지 구구단을 출력해보자.
gugu = 0
for i in range(2, 10):
  for j in range(1, 10):
    print(f"{i} x {j} = {i*j}")

 # 별 계단을 출력하는 코드를 작성해보자.
    # print("*")
    for i in range(1):
        print("*" * 1)
        for j in range(1):
            print("*" * 2)
            for k in range(1):
                print("*" * 3)
                for q in range(1):
                    print("*" * 4)
                    for w in range(1):
                        print("*" * 5)
#별 계단을 출력하는 코드를 작성해보자.
n = 5  # 계단의 줄 수 (입력값)
for i in range(1, n + 1):     # 1부터 n까지
    print("*" * i)

# 각 학생의 과목별 점수를 출력해보자.
scores = {
    "우빈": {"수학": 90, "영어": 85},
    "지민": {"수학": 100, "영어": 95},
    "하늘": {"수학": 80, "영어": 75}
}
#name, subject, score
for name, key_s in scores.items():
  for subject, score in key_s.items():
    print(f"{name}의 {subject}는 {score}야")

#아래와 같은 삼각형을 출력해보세요 (n = 5일 때)
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = 5
for i in range(1, n + 1):
    for j in range(1, i+1):
      print(j, end=' ')
    print()   #줄바꿈 역할

#각 학생의 점수를 보고 평균을 구해보세요.
students = {
    "우빈": [80, 90, 100],
    "지민": [70, 85, 95],
    "하늘": [60, 75, 85]
}
# name, score
for name, scores in students.items():
  print(f"{name}의 평균은{sum(scores)/len(scores)}")

#2차원 리스트의 요소를 하나씩 출력해보세요
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
  for num in row:
    print(num, end=" ")
  print()