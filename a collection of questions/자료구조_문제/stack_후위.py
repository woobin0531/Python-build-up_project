def 우선순위(연산자):
  if 연산자 == '+' or 연산자 == '-':
    return 1
  elif 연산자 == '*' or 연산자 == '/':
    return 2
  else:
    return 0

def 후위(식):
  스택 = []
  결과 = []

  for 문자 in 식:
    if 문자.isalnum():
      결과.append(문자)
    else:
      while 스택 and 우선순위(스택[-1]) >= 우선순위(문자):
        결과.append(스택.pop())
      스택.append(문자)

  while 스택:
    결과.append(스택.pop())

  return ''.join(결과)


print(후위('a+b*c'))

