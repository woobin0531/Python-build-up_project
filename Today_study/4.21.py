# 숫자 합 구하기
# 문제: 두 숫자를 입력받아 그 합을 반환하는 함수를 작성하세요.
def sum_two_numbers(x,y):
  return x + y
print(sum_two_numbers(3, 5))

# 문자열 길이 반환하기
# 문제: 주어진 문자열의 길이를 반환하는 함수를 작성하세요.
def string_length(x):
  return len(x)
print(string_length("Hello, World!"))

# 나이 계산하기
# 문제: 주어진 출생년도에서 나이를 계산하여 반환하는 함수를 작성하세요. (현재 년도는 2025년)
def calculate_age(x):
  a = 2025 - x
  return a
print(calculate_age(1995))

# 구구단 출력하기
# 주어진 숫자의 구구단을 출력하는 함수를 작성하세요.
def gugudan(x):
  for i in range(1, 10):
    print(f"{x}x{i} = {x * i}")
gugudan(3)

# 문자열에서 모음만 반환하기
# 주어진 문자열에서 모음(a, e, i, o, u)만 골라서 반환하는 함수를 작성하세요.
def extract_vowels(x):
  vowels = "aeiouAEIOU"
  result = ""
  for i in x:
    if i in vowels:
      result += i
  return result
extract_vowels("hello")

# 리스트에서 최대값과 최소값 구하기
# 주어진 리스트에서 최대값과 최소값을 구하여 반환하는 함수를 작성하세요.
def find_max_min(nums):
  if not nums:
    return None, None

  max_a = nums[0]
  min_a = nums[0]

  for num in nums:
    if num > max_a:
      max_a = num
    if num < min_a:
      min_a = num

  return max_a, min_a
print(find_max_min([3,1,2,3]))

# 문자열 반전하기
# 주어진 문자열을 뒤집은 값을 반환하는 함수를 작성하세요.
def reverse_string(x):
  print(x[::-1])
reverse_string("hello")