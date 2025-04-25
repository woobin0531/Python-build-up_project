# 가장 긴 문자열 찾기
# 아래 리스트에서 가장 길이가 긴 문자열을 출력하세요.
words = ["dog", "elephant", "cat", "hippopotamus", "lion"]
# 출력 예시: "hippopotamus"
most_list = []
for i in words:
  if len(i) > len(most_list):
    most_list = i
print(most_list)