클래스: 제품의 설계도
객체: 설계도로 만든 제품
속성: 클래스 안의 변수
메서드: 클래스 안의 함수
생성자: 객체를 만들 때 실행되는 함수
인스턴스: 메모리에 살아있는 객체

# example
class Monster:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def say(self):
    print(f"나는 {self.name} {self.age}살")
shark = Monster('상어', 7)
wolf = Monster('늑대', 3)

shark.say()
wolf.say()

# 쿠키 클래스 만들기
class Cookie:
  def __init__(self, flavor):
    self.flavor = flavor

  def bake(self):
    print(f"{self.flavor}쿠키가 구워졌어요!")

cookie1 = Cookie("초코")
cookie2 = Cookie("딸기")

cookie1.bake()
cookie2.bake()


# 포켓몬 클래스 만들기

class Pokemon:
    def __init__(self, name, ptype, level):
        self.name = name
        self.ptype = ptype
        self.level = level

    def attack(self):
        print(f"{self.name}이(가) 공격했다!")


# 포켓몬 객체 만들기
pokemon1 = Pokemon("이상해씨", "풀", 5)
pokemon2 = Pokemon("꼬부기", "물", 2)

pokemon1.attack()

# 포켓몬 레벨업, 진화 기능 추가

class Pokemon:
  def __init__(self, name, ptype, level):
    self.name = name
    self.ptype = ptype
    self.level = level

  def attack(self):
    print(f"{self.name}이(가) 공격했다")

  def level_up(self):
    self.level += 1
    print(f"{self.name}이(가) 레벨 {self.level}로 올랐다")

  def evolve(self):
    if self.level >= 10:
      print(f"{self.name}이(가) 진화했다")
      self.name = "진화된" + self.name
    else:
      print((f"{self.name}은 아직 진화할 준비가 안 됐어요"))

# 포켓몬 객체 만들기
pokemon1 = Pokemon("이상해꽃", "풀/독", 5)
pokemon2 = Pokemon("꼬부기", "물", 10)

# 공격하기
pokemon1.attack()
pokemon2.attack()

# 레벨업 테스트
pokemon1.level_up()

# 진화 테스트
pokemon1.evolve()
pokemon2.evolve()


# 동물 관리 클래스

class Animal:
    def __init__(self, name, ptype, age):
        self.name = name
        self.ptype = ptype
        self.age = age

    def eat(self):
        print(f"{self.name}(가)이 음식을 먹고있어요")

    def make_sound(self):
        print(f"{self.name}(가)이 소리를 내고 있어요")


lion = Animal("사자", "호랑이과", 5)
tiger = Animal("호랑이", "호랑이과", 4)

lion.eat()
tiger.make_sound()


# 동물원의 동물관리 기능

class Zookeeper:
    def __init__(self, name):
        self.name = name
        self.animal = []

    def add_animal(self, animal):
        self.animal.append(animal)
        print(f"{self.name}(가)이 {animal.name}(를)을 동물원에 추가했어요")

    def feed_animal(self, animal):
        print(f"{self.name}(가)이 {animal.name}에게 음식을 줬어요")
        animal.eat()

    def make_animal_sound(self, animal):
        print(f"{self.name}(가)이 {animal.name}에게 소리를 내게 했어요")


# 관리자와 동물들 만들기
zookeeper = Zookeeper("wb")
lion = Animal("사자", "호랑이과", 5)
tiger = Animal("호랑이", "호랑이과", 4)

# 동물들 추가하고 관리하기
zookeeper.add_animal(lion)
zookeeper.add_animal(tiger)

# 동물들에게 음식을 주고 소리를 내게 해보자!
zookeeper.feed_animal(lion)
zookeeper.make_animal_sound(tiger)


# 자동차 클래스 만들기
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} {self.model}의 속도가 {self.speed}km/h로 증가했습니다.")

    def brake(self):
        self.speed = 0
        print(f"{self.brand} {self.model}가 멈췄어요")


car1 = Car("현대", "아반떼")
car2 = Car("테슬라", "모델3")

car1.accelerate()
car1.accelerate()
car1.brake()
car2.accelerate()


# 도서관 책 클래스 만들기
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} 책이 대출되었습니다.")
        else:
            print(f"{self.title} 책은 이미 대출 중입니다.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} 책이 반납되었습니다.")
        else:
            print(f"{self.title} 책은 대출 중이 아닙니다.")


# 책 객체 만들기
book1 = Book("해리포터", "J.K. 롤링")
book2 = Book("어린왕자", "생텍쥐페리")

# 책 대출하기
book1.checkout()
book1.checkout()

# 책 반납하기
book1.return_book()
book1.return_book()

# 다른 책 대출해보기
book2.checkout()

# 1부터 n까지 홀수의 합 구하기
# 사용자에게 n을 입력받고,
# while문을 사용해 1부터 n까지 홀수만 더한 합을 출력하세요.
a = int(input())
i = 1
sum_a = 0

while i <= a:
    sum_a += i
    i += 2

print(sum_a)

# 특정 문자열 거꾸로 출력
# 문자열을 입력받아,
# while문을 사용해서 한 글자씩 거꾸로 출력하세요.
# (ex: 입력 "apple" → 출력 "e", "l", "p", "p", "a")
text = input("문자를 입력해주세요: ")
i = len(text) - 1

while i >= 0:
  print(text[i])
  i -= 1

# n부터 0까지 3씩 감소하며 출력
# 사용자에게 n을 입력받고,
# while문으로 n부터 0까지 3씩 감소시키면서 숫자를 출력하세요.
# (ex: n=10이면 10, 7, 4, 1 순으로 출력)
a = int(input("숫자를 입력해주세요: "))
b = []
while a >= 0:
  print(a)
  a -= 3

# 1부터 n까지의 합 구하기
# 사용자에게 양의 정수 n을 입력받고,
# while문을 사용해서 1부터 n까지의 총합을 구해서 출력하세요.
a = int(input())
sum_a = 0
i = 1

while i <= a:
  sum_a += i
  i += 1
print(sum_a)

# 입력한 숫자들의 평균 구하기
# 사용자에게 숫자를 계속 입력받다가,
# 입력값이 -1이면 입력을 종료하고,
# 지금까지 입력한 숫자들의 평균을 구해서 출력하세요.

b = 0
c = 0

while True:
  a = int(input("숫자를 입력해주세요(종료는 -1): "))
  if a == -1:
    break
  b += a
  c += 1

if c == 0:
  print("입력 숫자가 없습니다.")
else:
  avr = b / c
  print(f"평균은 {avr}입니다.")

# 5의 배수 찾기
# 사용자에게 양의 정수 n을 입력받고,
# while문을 사용해서 1부터 n까지 중에서 5의 배수만 출력하세요.
a = int(input())
i = 1

while i <= a:
  if i % 5 == 0:
    print(i)
  i += 1