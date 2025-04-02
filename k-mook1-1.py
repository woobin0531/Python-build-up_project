# 아래 문자열에서 숫자만 추출하여 모두 더하는 프로그램을 작성하세요
text = "The price of apple is 120 and banana is 80. Total is 200."
a = text.split( )   # text 를 공백을 기준으로 나누기
total = 0  # 숫자들을 합산하여 담을 공간
for i in a:
    i = i.strip(".")  #주의
    if i.isdigit():  # isdigit() 는 숫자인지 판별 후 합산
        total += int(i)  # 정수변환
print(total)