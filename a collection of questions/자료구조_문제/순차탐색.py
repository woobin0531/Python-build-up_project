# 자료구조_순차탐색
def sequential_search(A, key, low, high):
  for i in range(low, high+1):
    if A[i].key == key:
      return i
  return None