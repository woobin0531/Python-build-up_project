import random

과목이름들 = ["a", "b", "c", "d", "e", "f", "g", "h"]
과목들 = []

def 등급점수(점수):
    if 점수 >= 97:
        return 4.5
    elif 점수 >= 94:
        return 4.3
    elif 점수 >= 90:
        return 4.0
    elif 점수 >= 87:
        return 3.7
    elif 점수 >= 84:
        return 3.3
    elif 점수 >= 80:
        return 3.0
    elif 점수 >= 77:
        return 2.7
    elif 점수 >= 74:
        return 2.3
    elif 점수 >= 70:
        return 2.0
    elif 점수 >= 67:
        return 1.7
    elif 점수 >= 64:
        return 1.3
    elif 점수 >= 60:
        return 1.0
    else:
        return 0.0

for 과목명 in 과목이름들:
    점수 = random.randint(0, 100)
    학점 = random.randint(1, 3)
    과목들.append({"과목명": 과목명, "점수": 점수, "학점": 학점})

총점 = 0
총학점 = 0
출력내용 = ""

for 과목 in 과목들:
    점수 = 과목["점수"]
    학점 = 과목["학점"]
    환산 = 등급점수(점수)
    총점 += 환산 * 학점
    총학점 += 학점
    출력내용 += 과목["과목명"] + str(점수) + str(학점) + str(환산)

출력내용 += "총학점" + str(총학점)
출력내용 += "평균평점" + str(round(총점 / 총학점, 2)) if 총학점 > 0


# 파일 저장
with open("평균평점.txt", "w", encoding="utf-8") as 파일:
    파일.write(출력내용)

print("저장완료")
