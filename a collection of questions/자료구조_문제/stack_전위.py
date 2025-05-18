# 전위

def 우선순위(a):
  if a == '+' or a == '-':
    return 1
  elif a == '*' or a == '/':
    return 2
  else:
    return 0

def 전위(식):
  스택 = []
  결과 = []

  for 문자 in reversed(식):
    if 문자.isalnum():
      결과.append(문자)
    else:
      스택2 = []
      for 연산 in 스택:
        if 우선순위(문자) < 우선순위(연산):
          결과.append(연산)
        else:
          스택2.append(연산)
      스택 = 스택2
      스택.append(문자)

  for 연산 in reversed(스택):
    결과.append(연산)

  return ''.join(reversed(결과))


print(전위('a+b*c'))
