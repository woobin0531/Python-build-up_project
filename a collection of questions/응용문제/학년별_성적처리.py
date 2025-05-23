import random

def 데이터_만들기(학년수=6, 과목목록=["국어", "영어", "수학"]):
    학년별_과목점수 = {}
    for 학년 in range(학년수):
        학년이름 = f"{학년+1}학년"
        학년별_과목점수[학년이름] = {}
        반수 = random.randint(2, 10)
        for 반 in range(반수):
            반이름 = f"{반+1}반"
            학생수 = random.randint(10, 30)
            학년별_과목점수[학년이름][반이름] = []
            for 학생 in range(학생수):
                학생_점수 = {"이름": f"학생{학생+1}"}
                for 과목 in 과목목록:
                    학생_점수[과목] = random.randint(0, 100)
                학년별_과목점수[학년이름][반이름].append(학생_점수)
    return 학년별_과목점수, 과목목록

def 과목별_학년_평균(학년별_과목점수, 과목목록):
    for 학년이름, 반정보 in 학년별_과목점수.items():
        합 = {과목: 0 for 과목 in 과목목록}
        학생수 = 0
        for 반 in 반정보.values():
            for 학생 in 반:
                for 과목 in 과목목록:
                    합[과목] += 학생[과목]
                학생수 += 1
        print(f"[{학년이름}] 평균 점수")
        for 과목 in 과목목록:
            평균 = 합[과목] / 학생수 if 학생수 > 0 else 0
            print(f"- {과목} 평균은 {평균:.2f}입니다")
        print()

# 실행부

print("과목과 학년별 평균 결과입니다")
과목별_학년_평균(학년별_과목점수, 과목목록)

#함수화

import random

def 데이터_만들기(학년수=6, 과목목록=["국어", "영어", "수학"]):
    학년별_과목점수 = {}
    for 학년 in range(학년수):
        학년이름 = f"{학년+1}학년"
        학년별_과목점수[학년이름] = {}
        반수 = random.randint(2,10)
        for 반 in range(반수):
            반이름 = f"{반+1}반"
            학생수 = random.randint(10,30)
            학년별_과목점수[학년이름][반이름] = []
            for 학생 in range(학생수):
                학생_점수 = {"이름": f"학생{학생+1}"}
                for 과목 in 과목목록:
                    학생_점수[과목] = random.randint(0, 100)
                학년별_과목점수[학년이름][반이름].append(학생_점수)
    return 학년별_과목점수, 과목목록

def 과목별_학년_평균(학년별_과목점수, 과목목록):
    for 학년이름, 반정보 in 학년별_과목점수.items():
        합 = {과목: 0 for 과목 in 과목목록}
        학생수 = 0
        for 반 in 반정보.values():  # <-- .values()로 수정
            for 학생 in 반:
                for 과목 in 과목목록:
                    합[과목] += 학생[과목]
                학생수 += 1
        print(f"{학년이름} 평균점수")
        for 과목 in 과목목록:
            if 학생수 > 0:
                평균 = 합[과목] / 학생수
            print(f"{과목} 평균은 {평균:.2f}입니다")

# 데이터 생성 및 함수 호출
학년별_과목점수, 과목목록 = 데이터_만들기()
print("과목과 학년별 평균 결과입니다")
과목별_학년_평균(학년별_과목점수, 과목목록)