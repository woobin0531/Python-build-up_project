#List
-여러 요소를 한번에 작업할 수 있는 데이터 유형
-각 요소에 순차적으로 접근할 수 있음
 인덱스는 0부터 시작하며, 정수만 가능함
 인덱스를 음수로 부여하면 끝에서부터 접근
 slicing operator를 사용 지원
-요소를 변경할 수 있음
-요소를 추가할 수 있음
-list 간의 결합/연결 지원
-list를 반복 수행 지원

# List 함수 정리

# append() : 리스트 맨 뒤에 값을 추가하는 함수
guest_list = ["우빈", "수아"]
guest_list.append("현우")
print(guest_list)  # ['우빈', '수아', '현우']

# extend() : 리스트에 여러 개의 항목을 한꺼번에 추가
guest_list = ["우빈", "수아"]
new_guests = ["현우", "지민"]
guest_list.extend(new_guests)
print(guest_list) #['우빈', '수아', '현우', '지민']

#insert() : 리스트의 원하는 위치에 값을 삽입 / 리스트.insert(인덱스, 값) / 인덱스가 리스트보다 크면 끝에 추가
guest_list = ["우빈", "수아", "현우"]
guest_list.insert(0, "VIP손님")
print(guest_list)  # ['VIP손님', '우빈', '수아', '현우']

#remove() : 리스트에 지정한 값을 찾아서 삭제 / 리스트.remove(값)
guest_list = ["우빈", "현우", "수아", "현우"]
guest_list.remove("현우")
print(guest_list)  # ['우빈', '수아', '현우']

#pop() : 리스트에서 값을 꺼내고 삭제하는 함수 / 리스트.pop(인덱스)
guest_list = ["우빈", "수아", "현우"]
last_guest = guest_list.pop()
print(last_guest)  #'현우'
print(guest_list)  # ['우빈', '수아']

#clear() : 리스트 안에 있는 모든 요소를 한 번에 삭제 / 리스트는 남고, 안의 값들만 사라짐
guest_list = ["우빈", "수아", "현우"]
guest_list.clear()
print(guest_list)  # []

#index() : 리스트에서 특정 값이 처음 등장하는 위치를 반환
guest_list = ["우빈", "수아", "현우", "수아"]
pos = guest_list.index("수아")
print(pos)  # 1

#count() : 리스트 안에서 특정 값이 등장한 횟수를 반환 / 숫자도 가능
guest_list = ["우빈", "수아", "현우", "수아", "수아"]
print(guest_list.count("수아")   # 3

#sort() : 리스트의 값을 오름차순으로 정렬 숫자면 숫자크기 문자열이면 알파벳 순서
scores = [50, 30, 90, 10]
scores.sort()
print(scores) # [10, 30, 50, 90]
리스트.sort(reverse=True)  #내림차순 정렬

#reverse() : 리스트의 순서를 거꾸로 뒤집어주는 함수 정렬이 아니라 현재 순서를 반대로 뒤집는 것
guests = ["우빈", "수아", "현우"]
guests.reverse()
print(guests)  #['현우', '수아', '우빈']

#copy() : 리스트를 그대로 복사해서 새로운 리스트를 만듬 / 새리스트 = 기존리스트.copy()
guest_list = ["우빈", "수아", "현우"]
backup_list = guest_list.copy()
print(backup_list)  #['우빈', '수아', '현우']