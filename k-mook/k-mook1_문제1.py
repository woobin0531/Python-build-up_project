# 특정 단어 개수 세기
# 아래 문장에서 "Python"이 몇 번 나오는지 세어 출력하세요 (대소문자 구분 없이).
sentence = "Python is fun. I love python. PYTHON is powerful."
# 출력 예시: 3
a = sentence.lower().replace(".", "")
print(a.count("python"))