# 랜덤 볼링 게임 생성 및 점수 계산
# 요구사항
# 10프레임 볼링 게임을 랜덤으로 생성한다.
# 각 투구에서 쓰러뜨린 핀 수는 규칙에 맞게 랜덤으로 정한다.
# 첫 투구는 0~10 중 랜덤
# 스트라이크가 아니면 두 번째 투구는 남은 핀만큼 랜덤
# 10번째 프레임에서 스트라이크/스페어면 보너스 투구도 랜덤
# 생성된 투구 결과(점수목록)로 볼링 점수를 계산한다.

import random

def 랜덤_볼링_점수목록():
  점수목록 = []
  프레임 = 1

  while 프레임 <= 10:
    첫투구 = random.randint(0, 10)
    점수목록.append(첫투구)
    if 첫투구 == 10 and 프레임 < 10:
      프레임 += 1
      continue

    if 프레임 < 10:
      두번째투구 = random.randint(0, 10-첫투구)
      점수목록.append(두번째투구)
    else:  # 10프레임 보너스 처리
      두번째투구 = random.randint(0, 10-첫투구)
      점수목록.append(두번째투구)
      if 첫투구 == 10 or 첫투구 + 두번째투구 == 10:         # 스트라이크나 스페어면 보너스 투구 1회(스트라이크면 최대 2회)
        보너스1 = random.randinot(0, 10)
        점수목록.append(보너스1)
        if 첫투구 == 10 and 보너스1 == 10:
          보너스2 = random.randint(0, 10)
        else:
          보너스2 = random.randint(0, 10-보너스1)
        if 첫투구 == 10:
          점수목록.append(보너스2)
    프레임 += 1

  return 점수목록


def 볼링_점수계산(점수목록):
  총점 = 0
  투구위치 = 0
  프레임번호 = 1

  while 프레임번호 <= 10:
    if 점수목록[투구위치] == 10:
      프레임점수 = 10 + 점수목록[투구위치+1] + 점수목록[투구위치+2]   #스트라이크
      총점 += 프레임점수
      투구위치 += 1
    elif 점수목록[투구위치] + 점수목록[투구위치+1] == 10:
      프레임점수 = 10 + 점수목록[투구위치+2]  #스페어
      총점 += 프레임점수
      투구위치 += 2
    else:
      프레임점수 = 점수목록[투구위치] + 점수목록[투구위치+1]
      총점 += 프레임점수
      투구위치 += 2

    프레임번호 += 1
  print("총점: ", 총점)
  return 총점

점수목록 = 랜덤_볼링_점수목록()
볼링_점수계산(점수목록)