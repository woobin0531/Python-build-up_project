#정수를 하나 입력받아, 그 크기만큼 마름모 모양으로 별을 출력하시오.
n = int(input("정수를 입력하세여: "))
for i in range(1, 2*n):  # n = 3   i = 1, 2, 3, 4, 5
  if i <= n:
    별개수 = 2*i - 1
    공백 = n - i
  else:
    별개수 = 2 * (2*n - i) - 1
    공백 = i - n
  print(" "* 공백 + "*" * 별개수)

#사용자로부터 한 줄의 문장을 입력받고, 해당 문장에서 각 단어가 몇 번 등장하는지 세어 출력하는 프로그램을 작성하시오.
#(대소문자 구분 없이, 마침표/쉼표 제거)
a = input("문장을 입력하세요:")
# 문장에 대해서 순서대로 함수 먹이는거 가능하구나...
a = a.lower()
a = a.replace(",", "").replace(".", "")  # 연속으로 함수 먹이는게 가능하구나
words = a.split()
freq = {}  # 담을 그릇 만들기
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1
for word, count in freq.items():
  print(f"{word}: {count}")

#사용자로부터 문자열을 입력받아,
#해당 문자열의 각 문자를 검사한 뒤:
#소문자는 대문자로
#대문자는 소문자로
#그 외 문자(숫자, 기호)는 그대로
#바꿔서 출력하는 프로그램을 작성하시오.
text = input("문장을 입력하세요: ")
result = ""
for char in test:
  if char.islower():
    result += char.upper()
  elif char.isupper():
    result += char.lower()
  else:
    result += char
print(result)

#문자열을 입력받아서, 각 단어의 순서는 유지하되,
#각 단어의 글자만 거꾸로 뒤집어서 출력하는 프로그램을 작성하시오.
text = "Python is fun"
words = text.split()  # ["Python" "is" "fum"]
revers_words = [word[::-1] for word in words]
'''
revers_words = []
for word in words:
  revers_word = word[::-1]
  revers_words.append(revers_words)
'''
result = ' '.join(revers_words)
print(result)

#문자열을 입력받아서, 그 문자열 안에 있는 단어 수를 세는 프로그램을 작성하시오.
#단, 단어는 공백을 기준으로 구분되며, 연속된 공백도 하나의 공백으로 간주합니다.
a = input("입력:")
b = a.split()
c = len(b)
print(c)
print(b)

#사용자로부터 문자열을 입력받아서, 그 문자열이 회문(Palindrome)인지 판별하는 프로그램을 작성하시오.
a = input()
c_a = a.replace(" ", "").lower()
#print(c_a)
if c_a ==c_a[::-1]:
  print("Palindrome")
else:
  print("not Palindrome")