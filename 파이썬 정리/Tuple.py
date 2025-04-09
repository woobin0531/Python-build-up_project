#Tuple
'''
-괄호 없이도 선언 가능하며, 쉼표 , 가 없으면 tuple로 인식하지 않음
-선언 이후에는 내부 아이템을 변경할 수 없지만, 재할당은 가능함
 내부 아이템이 list인 경우에는 변경 가능
-아이템만을 삭제할 수 없음
my_tuple = (4, 2, 3, [6, 5])
my_tuple[1]= 9 #item 변경불가능

my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0]= 9
print(my_tuple) # 내부아이템이 list인 경우 변경가능
my_tuple = ('k', 'o', 'p', 'd')
print(my_tuple) #재할당은 가능
'''
#count(x) : x의 등장횟수를 반환
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # 3
print((5, 5, 5).count(5))  # 3

#index(x) : x가 처음 나타나는 인덱스를 반환
t = (10, 20, 30, 40)
print(t.index(30))  # 2
print((1, 2, 3, 2).index(2))  # 1
print(('a', 'b', 'c').index('c'))  # 2

#len(): 길이를 반환
print(len((1,2,3)))  # 3
print(len(()))  # 0
print(len(('apple', 'banana', 'cherry')))  # 3

#max(): 튜플에서 가장 큰 값을 반환
print(max((1, 5, 2)))  # 5
print(max(('a', 'c', 'b')))  # 'c'
print(max((10, 9, 11)))  # 11

#min(): 가장 작은 값을 반환
print(min((1, 5, 2)))  # 1
print(min(('a', 'c', 'b')))   # 'a'
print(min((10, 9, 11)))  # 9

#sum(): 모든 숫자 요소의 합을 반환
print(sum((1, 2, 3)))   # 6
print(sum((5, 5, 5, 5)))  # 20
print(sum((100,)))  #100

#sorted(): 튜플을 정렬된 리스트로 반환(튜플 자체는 변하지 않음)
print(sorted((3, 1, 2)))  # [1, 2, 3]
print(sorted(('b', 'c', 'a')))  # ['a', 'b', 'c']