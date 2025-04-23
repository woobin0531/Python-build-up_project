#문자열을 입력받아 팰린드롬인지 판별하라.
#*팰린드롬이란 거꾸로 읽어도 똑같은 문장 또는 단어​
#	Ex) ‘기러기’, ’mom’ 등
#조건​:
#대소문자 구분 X
#공백 무시

A=input("팰린드롬을 판별할 문자열을 입력하세요 \n")
def palindrome(a):
    new = a.lower()
    new = a.replace(" ", "")
    return new == a[::-1]
palindrome(A)
반환값 : True or False