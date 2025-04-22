#여러 개의 단어로 이루어진 배열이 주어집니다.
#또한 slices 라는 배열이 주어 집니다.
#각 단어에서 특정 구간(부분 문자열)을 잘라 조합하여
# "polytech"가 나오도록 코드를 짜보시오

words = ["apocalypse", "meteorology", "architect", "cheetah"]
slices = [[(1, 2), (5, 6)], [(2, 3)], [(2, 2)], [(1, 1)]]
answer = ""

for i in range(len(slices)):
    for j, k in slices[i]:
        answer += words[i][j:k+1]
print(answer)
