# strip()-양쪽 공백 제거
print("  hello  ".strip())       # hello
print("\nPython\n".strip())      # Python
print("   trimmed text   ".strip())  # trimmed text
#strip()은 양쪽의 모든 공백문자(' ', \n, \t, \r등) 제거, 중간은 건들지 않음

# split()-문자열을 리스트로 나누기
print("a,b,c".split(","))         # ['a', 'b', 'c']
print("apple orange banana".split()) # ['apple', 'orange', 'banana']
print("1|2|3|4".split("|"))       # ['1', '2', '3', '4']
#문자열은 나누면 리스트로~

#뒤에 있는 두 번째 2는 어떻게 찾을까?
t = (1, 2, 3, 2)
first_index = t.index(2)         # 1  ,
second_index = t.index(2, first_index + 1)
print(second_index)              # 3

#뒤에 있는 두 번째 2는 어떻게 찾을까?  enumerate() 사용
num = [10, 20 ,30 ,40, 66, 33]
indexs = [i for i, v in enumerate(num) if v % 2 == 1]
print(indexs)

print(len(('a',)))      # 1 → 요소가 1개 (주의: 꼭 콤마 붙여야 튜플임!)

#sorted(): 튜플을 정렬된 리스트로 반환(튜플 자체는 변하지 않음)
print(sorted((3, 1, 2)))  # [1, 2, 3]
print(sorted(('b', 'c', 'a')))  # ['a', 'b', 'c']

#정수형(int) 이나 집합(set), 딕셔너리(dict) 는 슬라이싱이 안됨
num = 12345
print(num[0:2])     # 에러: slicing 불가
my_set = {1, 2, 3}
print(my_set[0:2])  # 에러: slicing 불가

a = {1, 2, 3, 4, 5}
b = {3, 4, 5}
result = a.difference(b)
print(result)