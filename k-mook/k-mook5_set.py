Set(집합)
-수학에서의 집합과유사
-빈집합은 set(), {}를 사용해서 요소값 입력
-리스트와 마찬가지로 값의 모임이지만 순서는 없음
-중복되지 않고 저장됨
-결과값이 순서없이 저장되기 때문에 다시 실행시킨 후 결과를 확인하면 순서가 다르게 나타날수 있음

ex) s1 = set("banana")
print(s1) #{'b', 'a', 'n'}
-집합함수
 in/ not in: 세트 안에 값이 있는지 여부를 확인( True, False)
 fruit = {"apple", "banana", "carrot"}
 "apple" in fruit # True

 add() : 세트안에 값을 하나만 추가
 fruit = {"apple", "banana", "carrot"}
 fruit.add("melon")
 # {'melon', 'apple', 'banana', 'carrot'}

 update() : 세트안에 값을 여러 개 추가
 fruit = {"apple", "banana", "carrot"}
 fruit.update(["orange', 'watermelon"])
 # {'orange', 'watermelon', 'apple', 'banana', 'carrot'}

 discard() : 세트 안에 있는 항목 삭제
 fruit = {"apple", "banana", "carrot"}
 fruit.discard("carrot")
 # {'apple', 'banana'}

 remove(): 세트 안에 있는 항목 삭제 / 없는 항목을 삭제할 때에는 에러 발생
 fruit = {"apple", "banana", "carrot"}
 fruit.remove("banana")
 fruit.remove("banana")
 #{apple, banana}
 error

 clear(): 세트 안에 있는 값 삭제
 fruit = {"apple", "banana", "carrot"}
 fruit.clear()

 del(): 세트 자체를 삭제
