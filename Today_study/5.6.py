# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록
# solution 함수를 완성해보세요

def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
# a는 0, b는 1, c는 2, ..., j는 9입니다.
# 예를 들어 23살은 cd, 51살은 fb로 표현합니다.
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를
# return하도록 solution 함수를 완성해주세요.

def solution(age):
    result = ''
    for ch in str(age):
        result += chr(ord('a') + int(ch))
    return result

# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한
# 배열을 return하도록 solution 함수를 완성해주세요.

def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(e) + 1 for e in emergency]

solution([3, 2, 7])

# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로
# (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때
# 두 숫자의 곱이 n인 자연수 순서쌍의 개수를
# return하도록 solution 함수를 완성해주세요.

def solution(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# 개미 군단이 사냥을 나가려고 합니다.
# 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
# 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다.
# 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만,
# 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다.
# 사냥감의 체력 hp가 매개변수로 주어질 때,
# 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를
# return하도록 solution 함수를 완성해주세요.

def solution(hp):
    a = hp // 5
    hp %= 5

    b = hp // 3
    hp %= 3

    c = hp

    return a + b + c

