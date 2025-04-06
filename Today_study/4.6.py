#아래 리스트에서 "apple"이라는 단어가 몇 개 있는지 세고,처음 등장하는 위치(인덱스) 도 구하시오
fruits = ["banana", "apple", "cherry", "apple", "grape", "apple"]
print(fruits.count('apple'))
print(fruits.index('apple'))

#다음 리스트에서 "kiwi"를 "mango" 앞에 추가하시오.
fruits = ['apple', 'banana', 'mango']
fruits.insert(2, 'kiwi')
print(fruits)

'''아래 리스트에서 "peach" 항목을 삭제하고,
마지막 항목을 꺼낸 후 출력하시오.
마지막에 남은 리스트도 출력하세요.'''

fruits = ["peach", "apple", "banana", "cherry"]
fruits.remove('peach')
print(fruits)
print(fruits.pop())
print(fruits)

#쇼핑카트에 담긴 물건 목록에서 "콜라"가 몇 개인지 세고, "콜라"를 "제로콜라"로 모두 바꾸시오.
cart = ["콜라", "사이다", "콜라", "오렌지주스", "콜라"]
print(cart.count("콜라"))
for i in range(len(cart)):
  if cart[i] == "콜라":
      cart[i] = "제로콜라"
print(cart)

#학생 점수 리스트에서 60점 미만은 탈락, 60점 이상은 **"합격"**을 출력하시오.
scores = [45, 67, 89, 32, 76]
for i in scores:
  if i < 60:
    print("탈락") #print(f'{i}점: 탈락')
  else:
    print("합격") #print(f'{i}점: 합격')

#가게 매출 리스트에서 총 매출을 구하고, 최고 매출과 최저 매출도 함께 출력하시오.
sales = [120000, 300000, 175000, 250000, 98000]
총매출 = sum(sales)
print(총매출)
print("최고매출:",max(sales))
print("최저매출:", min(sales))

#정수로 이루어진 리스트 nums = [3, 6, 9, 12, 15, 18, 21]가 주어졌을 때
#짝수만 골라서 새로운 리스트로 만들어 출력하라.

nums = [3, 6, 9, 12, 15, 18, 21]
items = []
for i in nums:
  if i % 2 == 0:
    items.append(i)
print(items)

#data = [1, 2, 3, 4, 5] 리스트가 주어졌을 때,
#이 리스트를 반대로 뒤집은 새로운 리스트를 만들어 출력하라.

data = [1, 2, 3, 4, 5]
data1 = data[::-1]
print(data1)

#리스트 names = ["우빈", "지민", "정국", "우빈", "지민"]에서
#중복을 제거한 리스트를 만들어 출력하라. (단, 순서는 유지)

names = ["우빈", "지민", "정국", "우빈", "지민"]
names1 = []
for i in names:
  if i not in names1:
    names1.append(i)
print(names1)

#다음 튜플의 길이를 구하는 코드를 작성하세요.
colors = ("red", "green", "blue", "yellow")
print(len(colors))

#다음 튜플에서 첫 번째 값과 마지막 값을 출력하는 코드를 작성하세요.
fruits = ("apple", "banana", "cherry", "orange")
print(fruits[0],fruits[3])

#다음 리스트를 튜플로 변환하고, 다시 튜플을 리스트로 변환해보세요.
nums = [1, 2, 3, 4, 5]
t_nums = tuple(nums)
print(type(t_nums))
l_nums = list(t_nums)
print(type(l_nums))

# animals 튜플의 값을 하나씩 출력해보세요.
animals = ("dog", "cat", "rabbit")
for i in animals:
  print(i)

# 두 튜플을 연결해서 새로운 튜플로 만들어보세요.
a = (1, 2, 3)
b = (4, 5, 6)
print(a+b)

# 30이 튜플 안에 있는지 확인해보세요.
nums = (10, 20, 30, 40)
for i in nums:
  if i == 30:
    print("확인")

# nums 튜플에서 짝수만 골라 새로운 리스트로 만들어보세요.
nums = (1, 2, 3, 4, 5, 6)
nums2 = []
for i in nums:
  if i % 2 == 0:
    nums2.append(i)
print(nums2)

# 튜플의 모든 값을 더해서 출력해보세요.
numbers = (5, 10, 15, 20)
print(sum(numbers))

# 최고 점수와 최저 점수를 각각 출력해보세요.
scores = (88, 95, 70, 100, 99)
print(max(scores), min(scores))