# 자료구조_선택정렬
def selection_sort(A):
  n = len(A)
  for i in range(n-1):
    least = i;
    for j in range(i+1, n):
      if (A[j]<A[least]):
        least = j
    A[i], A[least] = A[least], A[i]
    printStep(A, i + 1)

def printStep(arr, val):
  print("Step %2d = " % val, end="")
  print(arr)

selection_sort([11, 25, 45, 22, 4, 6])