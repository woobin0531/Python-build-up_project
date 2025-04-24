class Person:
    def __init__(self, name, age):
        self.name = name      # 속성
        self.age = age        # 속성

    def greet(self):
        print(f"안녕하세요, 저는 {self.name}이고, 나이는 {self.age}살입니다.")
p1 = Person("철수", 25)
p2 = Person("영희", 30)

p1.greet()  # 안녕하세요, 저는 철수이고, 나이는 25살입니다.
p2.greet()  # 안녕하세요, 저는 영희이고, 나이는 30살입니다.
-----
class Person:
  def __init__(self):
    self.hello = '안녕하세요.'

  def greeting(self):
    print(self.hello)

james = Person()
james.greeting()
------
class Person:
  def __init__(self, name, age, address):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.address = address

  def greeting(self):
    print("{0} 저는 {1}입니다".format(self.hello, self.name))

maria = Person("마리아", 20, '서울시 서초구')
maria.greeting()

print("이름:", maria.name)
print("나이:", maria.age)
print("주소:", maria.address)
-----
class Person:
  def __init__(self, *args):
    self.name = args[0]
    self.age = args[1]
    self.address = args[2]
maria = Person(*['마리아', 20, '서울시 서초구'])
----
class Person:
  def __init__(self, **kwargs):
    self.name = kwargs['name']
    self.age = kwargs['age']
    self.address = kwargs['address']

maria1 = Person(name = '마리아', age = 20, address = '서울')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울'})
------
# 비공개 속성(private attribute)
class Person:
  def __init__(self, name, age, address, wallet):
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet

maria = Person('마리아', 20, '서울시 서초구')
maria.__wallet -= 10000