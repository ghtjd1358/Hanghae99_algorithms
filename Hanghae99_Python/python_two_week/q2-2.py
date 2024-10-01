# 문제 이해 : 

# 접근 방법:
#   빈 배열 생성
#   입력 받은 값을 split(' ')을 사용하여 배열로 join, reverse하면 될 것 같다.
#   케이스 번호는 입력 받은 n개의 값을 붙이면 될 듯한한데 알파벳 L 조건은 무시해도 될 것 같다.

import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1, N+1):
    word = input().strip().split()
    words = ' '.join(reversed(word))

    print(f"Case #{i}: {words}")#Case #{i}: <- ' : ' 여기 부분 띄우면 오답...