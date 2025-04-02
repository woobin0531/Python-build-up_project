sentence = "I love Python. Python is fun. Python is powerful!"
a = sentence.count("Python")  #단어 갯수 세기
b = sentence.replace("Python", "java") ## "Python"을 "Java"로 변경
c = b.split(".")  # 마침표(".")를 기준으로 문장을 나누어 리스트로 변환
print(c)