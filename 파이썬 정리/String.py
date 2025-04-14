# 문자열(string) 함수 정리

# lower()-모두 소문자로 바꾸기
print("HELLO".lower())         # hello
print("Python RULES!".lower()) # python rules!
print("123ABC".lower())        # 123abc

# upper()-모두 대문자로 바꾸기
print("hello".upper())         # HELLO
print("Python rules!".upper()) # PYTHON RULES!
print("abc123".upper())        # ABC123

# strip()-양쪽 공백 제거
print("  hello  ".strip())       # hello
print("\nPython\n".strip())      # Python
print("   trimmed text   ".strip())  # trimmed text
'''
strip()은 양쪽의 모든 공백문자(' ', \n, \t, \r등) 제거, 중간은 건들지 않음
'''

# replace(old, new)-문자열 일부 바꾸기
print("banana".replace("a", "o"))     # bonono
print("2025-04-10".replace("-", "/")) # 2025/04/10
print("Python is fun".replace("fun", "awesome")) # Python is awesome

# find(sub)-부분 문자열 찾기(위치 반환)
print("banana".find("na"))    # 2 (처음 등장 위치)
print("hello world".find("o"))# 4
print("test".find("x"))       # -1 (없으면 -1)

# split()-문자열을 리스트로 나누기
print("a,b,c".split(","))         # ['a', 'b', 'c']
print("apple orange banana".split()) # ['apple', 'orange', 'banana']
print("1|2|3|4".split("|"))       # ['1', '2', '3', '4']

# join()-리스트를 문자열로 합치기
print(",".join(['a', 'b', 'c']))      # "a,b,c"
print(" ".join(["hello", "world"]))  # "hello world"
print("-".join(["2025", "04", "10"])) # "2025-04-10"

# startswith()-특정 문자(열)로 시작하는지 확인
print("hello".startswith("he"))    # True
print("banana".startswith("ba"))   # True
print("data.csv".startswith("img"))# False

# endswith()-특정 문자(열)로 끝나는지
print("photo.jpg".endswith(".jpg"))   # True
print("report.pdf".endswith(".txt"))  # False
print("music.mp3".endswith("3"))      # True

# isdigit()-숫자로만 구성되어 있는지
print("12345".isdigit())       # True
print("12a45".isdigit())       # False
print("007".isdigit())         # True

# isalpha()-알파벳으로만 구성되어 있는지
print("abc".isalpha())         # True
print("abc123".isalpha())      # False
print("Hello".isalpha())       # True

# islower()-모두 소문자인지
print("hello".islower())       # True
print("Hello".islower())       # False
print("python3".islower())     # True

# isupper()-모두 대문자인지
print("HELLO".isupper())       # True
print("Hello".isupper())       # False
print("PYTHON".isupper())      # True

# len()-문자열 길이
print(len("hello"))       # 5
print(len("  hello  "))   # 9 (공백도 포함)
print(len(""))            # 0

# swapcase()- 대소문자 바꾸기
text = "PyTHon Is FuN"
print(text.swapcase())  # 출력: 'pYthON iS fUn'
