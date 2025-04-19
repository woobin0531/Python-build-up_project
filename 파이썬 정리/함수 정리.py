1. 함수란?
함수는 여러 줄의 코드를 하나의 이름으로 묶어 재사용할 수 있게 하는 도구.
예를 들어 라면을 끓이는 과정을 함수로 만들면, 매번 "물 끓이기 -> 면 넣기 -> 스프넣기"를 코드로 안 써도
되고, make_ramen()만 호출하면 됨
즉, 복잡한 일을 하나의 이름으로 줄어주는 것이 함수
def say_hello():
    print("안녕")
-def는 함수를 정의한다는 뜻(define의 줄임말)
-say_hello()는 함수 이름, ()안에는 필요한 값을 넣는 자리(매개변수)
-print("안녕")는 이 함수가 실행할 코드

2. 함수의 구성요소
#함수정의
def 함수이름(매개변수):
    실행할 코드
    return 변환값
#함수호출
함수이름(값1, 값2)
-이걸 실행하면 함수 내부의 코드가 작동
-괄호 안 값이 위에서 말한 매개변수로 전달됨

3. return의 의미와 사용
-return 은 계산한 값을 함수 바깥으로 내보내는 역할
-반대로 print()는 그저 화면에 보여줄 뿐, 값을 전달하지
print(않는다)

def add(x, y):
    return x + y
result = add(3, 4)  # result는 7
-만약 return 없이 print(x + y)만 했다면, 화면엔 7이 찍히지만 result에는 아무 것도 안담겨 (그땐 None이라는 값이 들어감)
why return이 필요한가?
-계산한 결과를 저장하거나 다른 코드에 넘겨서 쓸 수 있기 때문
-예를 들어 계산기 만들 땐 계산 결과를 다른 연산에 써야 하니까 꼭 return이 필요해

def say_hi():
    print("Hi!")
result = say_hi()   # 화면엔 "Hi!"가 찍히지만, result는 None

4. 기본값 매개변수
def greet(name="손님"):
    print(f"안녕하세요, {name}님!")

greet()        # 안녕하세요, 손님님!
greet("우빈")   # 안녕하세요, 우빈님!
- name ="손님" 처럼 기본값을 정해두면, 값을 안 넣었을 때 자동으로 그 값이 들어감
- 값을 넣으면 그 값이 사용되고 안 넣으면 기본값이 사용됨

5. 요약
함수는 코드 묶음이다 (재사용, 정리)

매개변수로 입력값을 받아서 처리할 수 있다

return은 값을 밖으로 전달한다 (없으면 None)

print()는 화면 출력만, 저장은 안 됨

기본값 인자 사용 가능

조건문, 반복문과 함께 조합하여 실용적인 함수 구현 가능

**우빈의 궁금증들(괄호, return, 값 전달, 기본값 등)**은 모두 함수의 작동 원리를 이해하면 해결됨!

