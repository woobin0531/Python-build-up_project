# Dictionary
"""
닥셔너리: 키와 값이 쌍으로 구성되어 있는 자료구조
-dict() 생성자로 정의하거나 혹은 직접 사전을 생성
-중괄호로 표현, 키와 값은 콜론(;)으로 구분하고 요소는 콤마로 구분

키(key)
-세트처럼 중복된 값을 가질 수 없고, 튜플처럼 변경이 불가능
-리스트를 키로 사용할 수 없음

값(value)
-키에 대한 값을 수정, 삭제 가능
-리스트, 튜플, 세트 등을 값으로 사용가능

딕셔너리 특징
-값 조회 시 순차적으로 지정하지 않기 때문에 검색 속도가 빠름
-index를 지원하지 않으며, 없는 키를 사용하면 에러 발생
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
type(dclass)
dclass[1]
<class "dict">
{1: "apple", 2: "banana", 3: "carrot"}

"""
키 값에는 리스트가 입력되지 않음
"""
ex)
j_dict = {[1, "가넷"]: "진실, 우정"}
 #error
j_dict = {(1, "가넷"): "진실, 우정"}
# {(1: '가넷'):'진실, 우정'}

"""
새로운 항목을 추가하려면 새로운 키와 값을 할당해야 함
"""
dclass = {1:"apple", 2:"banana", 3:"carrot"}
dlcass[4] = "melon"
# {1:'apple', 2:'banana', 3:'carrot', 4:'melon'}
2 in dclass  # in/ not in: 딕셔너리 안에 키가 있는지 여부를 확인(True, False)
# True
"apple" in dclass
# False
"""
딕셔너리 함수
item(): 딕셔너리에서 key-value를 리스트형태로 한 쌍으로 가져오는 것
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
# dict_items([(1:'apple'), (2:'banana'), (3:'carrot')])

"""
keys(): 딕셔너리에서 리스트형태로 key 값만 가져오는 것
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
dclass.keys()
# dict_keys([1, 2, 3])

"""
values(): 딕셔너리에서 리스트형태로 value값만 가져오는 것
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
dclass.values()
# dict_values(['apple', 'banana', 'carrot'])

"""
get(a): 딕셔너리에서 key(a)로 값을 확인
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
dlcass.get(1)  # apple
dlcass.get(4)  # None
dclass.get(4, "melon")  # melon
dclass  # {1:'apple', 2:'banana', 3: 'carrot'}

"""
pop(): 해당 값을 추출하고 딕셔너리에서 삭제 / 리스트와 비슷하나 키 값이 필요함
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot", 4:"melon"}
dclass.pop(1)  # 'apple
dclass  # {2: 'banana', 3:'carrot', 4:'melon'}
dclass.pop(1)  # error

"""
clear(): 딕셔너리 안의 전체 값을 삭제
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
dclass.clear()
dclass  # {}

"""
del A[key]: 딕셔너리의 key를 삭제
"""
ex)
dclass = {1:"apple", 2:"banana", 3:"carrot"}
del dclass[1]
dclass # {2:'banana', 3:'carrot', 4:'melon'}

"""
sorted 함수로 요소 정렬
"""
ex)
dlcass = {1:"apple", 2:"banana", 3:"carrot"}
sorted(dlcass)  # [1, 2, 3]
sorted(dclass.kets()) #  [1, 2, 3]
sorted(dclass.values())  # ['apple', 'banana', 'carrot']


