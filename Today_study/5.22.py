# 자료구조_이진탐색
def binary_search(A, key, low, high):
  if (low <= high):
    middle = (low + high) // 2
    if key == A[middle].key:
      return middle
    elif (key<A[middle].key):
      return binary_search(A, key, low, middle - 1)
    else:
      return binary_search(A, key, middle + 1, high)
  return None

# 자료구조_이진탐색
def binary_search_iter(A, key, low, high):
  while (low <= high):
    middle = (low + high) // 2
    if key == A[middle].key:
      return middle
    elif (key > A[middle].key):
      low = middle + 1

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

# 자료구조_삽입정렬
def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i-1
    while j >= 0 and A[j] > key:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = key
    printStep(A, i)

# 자료구조_버블정렬
def bubble_sort(A):
  n = len(A)
  for i in range(n-1, 0, -1):
    bChanged = False
    for j in range(i):
      if (A[j]> A[j+1]):
        A[j], A[j+1] = A[j+1], A[j]
        bChanged = True
    if not bChanged: break;
    printStep(A, n-1)

# 자료구조_순차탐색
def sequential_search(A, key, low, high):
  for i in range(low, high+1):
    if A[i].key == key:
      return i
  return None