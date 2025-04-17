# 두 문장의 공통 단어 찾기
# 아래 두 문장에서 공통으로 등장하는 단어만 set으로 출력하세요.
sentence1 = "I love Python and data science"
sentence2 = "Python is great for data analysis"
a = sentence1.split(" ")
b = sentence2.split(" ")
c = set(a)&set(b)
print(c)

# 알파벳만 골라 정리
# 아래 문자열에서 알파벳 문자만 골라 set으로 출력하세요 (중복 제거)
text = "Hello123, World! Welcome to 2025."
english = []

for i in text:
  if i.isalpha():
    english.append(i)
print(set(english))

# 원소가 3개 이상인 집합만 출력하기
# 아래 리스트 안의 여러 set 중, 원소가 3개 이상인 집합만 출력하세요.
sets = [
    {1, 2, 3},
    {4, 5},
    {6, 7, 8, 9},
    {10}
]
ff = []
for i in sets:
  if len(i)>= 3:
    ff.append(i)
print(ff)

# 1~10 사이 숫자 하나 뽑기
# 1부터 10 사이의 숫자 중 무작위로 하나를 출력하세요.
import random
a = random.randint(1,10)
print(a)

# 리스트에서 랜덤 추첨
# 아래 리스트에서 사람 한 명을 무작위로 골라 출력하세요.
names = ["Anna", "Ben", "Clara", "David", "Ella"]
import random
a = random.choice(names)
print(a)

# 리스트 무작위 섞기
# 아래 숫자 리스트를 무작위로 섞은 후 출력하세요.
import random
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

# 로또 번호 생성기
# 1부터 45까지의 숫자 중 무작위로 6개를 뽑아 출력하세요.
# 숫자는 중복 없이, 오름차순으로 정렬되어야 합니다.
import random
q = sorted(random.sample(range(1,46), 6))
print(q)

# 랜덤 비밀번호 생성기
# 알파벳 소문자 중 무작위로 8개의 문자를 뽑아 비밀번호처럼 이어 붙여 출력하세요.
import random
import string
password = ''.join(random.choices(string.ascii_lowercase, k = 8))
print(password)

#함수
-어떤 작업을 수행하는 코드 블록
-특정 입력(인자)을 받아서, 어떤 처리를 한 뒤 결과를 내보냄

#왜 사용할까?
-재사용 가능: 한 번 만들어 놓으면 여러 번 사용할 수 있다.
-가동성 향상: 코드를 기능별로 나눠서 더 보기 좋고 이해하기 쉬움
-유지보수 용이: 수정할 부분이 있을 때 함수만 고치면 됨
# 기본 구조
def 함수이름(매개변수1, 매개변수2, ...):
  실행할 코드
  return 반환값

def make_ramen(name):
  print("물 끓이는 중")
  print(f"{name} 끓이는 중..")
  return f"{name} 완성!"

result = make_ramen("신라면")
print(result)

def make_egg_fry(egg_count):
  if egg_count <= 0:
    print("계란이 없습니다!")
    return

  print("팬 예열중")

  for i in range(1, egg_count + 1):
    print(f"계랸{i}개 깨는중..")
  print("지글지글 굽는 중...")
  print("뒤집는 중...")

  return f"{egg_count}개 계란후라이가 완성되었습니다!"

result = make_egg_fry(3)
print(result)


def make_toast(장):
  print("토스트기 예열중...")
  print("(식빵 개수만큼 반복)")
  for i in range(1, 장 + 1):
    print(f"-식빵 {i}장 굽는 중..")
  return "굽기완료"
result = make_toast(5)
print(result)


def make_toast(장):
    if 장 <= 0:
        print("식빵이 없습니다")
        return

    print("토스터기 예열 중...")

    for i in range(1, 장 + 1):
        print(f"식빵 {i}장 굽는 중...")

    print("굽기 완료!")
    return f"{장}장의 토스트가 완성되었습니다!"


result = make_toast(3)
print(result)