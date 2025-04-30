# 튜플 인덱싱
# 아래의 튜플에서 세 번째 요소를 출력하세요.
fruits = ('apple', 'banana', 'cherry')
print(fruits[2])

# 튜플 언패킹
# 아래의 튜플을 각각 변수 x, y, z에 언패킹해서 출력하세요.
t = (100, 200, 300)
x, y, z = t
print(x)
print(y)
print(z)

# 튜플 슬라이싱
# 아래 튜플에서 (3, 4, 5)만 슬라이싱해서 출력하는 코드를 작성하세요.
nums = (1, 2, 3, 4, 5, 6)
print(nums[2:4])

# 튜플 내장함수 활용
# 아래 튜플에서 요소의 개수, 최대값, 최소값을 각각 출력하는 코드를 작성하세요.
scores = (87, 92, 100, 76, 88)
print("요소의 개수",len(scores))
print("최대값", max(scores))
print("최소값", min(scores))

# 리스트와 튜플 변환
# 아래 리스트를 튜플로 변환하고, 다시 리스트로 변환하는 코드를 작성하세요.
data = [10, 20, 30, 40]
t_data = tuple(data)
r_data = list[t_data]

# 튜플 불변성 우회 및 값 변경
# 튜플은 불변(immutable) 자료형이기 때문에 요소를 직접 변경할 수 없습니다.
# 아래 튜플에서 두 번째 값을 99로 바꾼 새로운 튜플을 만드는 코드를 작성하세요.
t = (10, 20, 30, 40)
a = list(t)
a[1] = 99
b = tuple(a)
print(b)

# 튜플 불변성 우회 및 값 변경
# 튜플은 불변(immutable) 자료형이기 때문에 요소를 직접 변경할 수 없습니다.
# 아래 튜플에서 두 번째 값을 99로 바꾼 새로운 튜플을 만드는 코드를 작성하세요.
t = (10, 20, 30, 40)
new_t = t[:1] + (99,) + t[2:]
print(new_t)

# 튜플 언패킹과 함수 반환값 활용
# 두 개의 정수를 입력받아, 그 합, 차, 곱, 몫, 나머지를 튜플로 반환하는 함수를 작성하고,
# 반환된 튜플을 언패킹하여 각각의 값을 출력하세요
def calc(a, b):
  return (a + b, a - b, a * b, a // b, a % b)

result = calc(20, 7)
_sum, diff, prod, quot, remain = result

print("합:", _sum)      # 27
print("차:", diff)      # 13
print("곱:", prod)      # 140
print("몫:", quot)      # 2
print("나머지:", remain) # 6

# 튜플 컴프리헨션(표현식) 활용
# 1부터 20까지의 수 중에서 3의 배수만을 포함하는 튜플을 한 줄의 코드로 생성하세요.
result = tuple(x for x in range(1, 21) if x % 3 == 0)
print(result)
