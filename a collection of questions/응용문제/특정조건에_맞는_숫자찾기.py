#설명 : 정수 n이 주어졌을 때,
#1부터 n까지의 숫자 중에서 3의 배수 이면서 2의 배수가 아닌 수들만 리스트에 담아 반환하는 함수를 작성하세요
#입력 예시 : solution(20)
#출력 예시 : [3, 9, 15, 21]
#조건 :
#n은 1이상 1000이하의 자연수입니다.
#3의 배수이면서, 2의 배수가 아닌 수만 포함되어야 합니다.

def 정수(n):
  a = []
  for i in range(1, n+1):
    if i % 6 == 0:
      except
    if i % 3 == 0:
      a.append(i)
  return a
  ----------


def 정수(n):
    a = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 6 != 0:
            a.append(i)
    return a
