#다음 문자열에서 "Python"이라는 단어가 몇 번 나오는지 세고,
# 모든 "Python"을 "Java"로 변경한 후 리스트로 나누어 출력하세요.

sentence = "I love Python. Python is fun. Python is powerful!"
a = sentence.count("Python")  #단어 갯수 세기
b = sentence.replace("Python", "java") ## "Python"을 "Java"로 변경
c = b.split(".")  # 마침표(".")를 기준으로 문장을 나누어 리스트로 변환
print(c)