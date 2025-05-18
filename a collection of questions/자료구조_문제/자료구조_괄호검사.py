def 괄호검사(문자열):
  스택 = []
  괄호쌍 = {')': '(', ']': '[', '}': '{'}

  for 문자 in 문자열:
    if 문자 in '([{':
      스택.append(문자)
    elif 문자 in ')]}':
      if not 스택 or 스텍[-1] != 괄호쌍[문자]:
        return False
      스택.pop()
  return len(스택) == 0

print(괄호검사("()"))         # True
print(괄호검사("([])"))       # True
print(괄호검사("({[)]}"))     # False
print(괄호검사("("))          # False
print(괄호검사("({[]})"))     # True