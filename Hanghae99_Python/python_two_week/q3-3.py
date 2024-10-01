# 입력
# 첫번째 줄 : N = 음을 아는 노래의 개수, M = 맞추기를 시도할 노래 개수
# 두번째 줄부터 N 개 줄에 걸쳐서 노래 제목의 길이 T , 영어 대소문자로 이루어진 문자열 노래제목 S
# 처음 등장하는 일곱개의 음이름 a1~a7 공백으로 구분 됫 ㅓ주어짐

# N+2 번째 줄부터 M 개 줄에 걸쳐서 정환이가 맞히기를 시도할 노래의 첫 세음 b1~b3 a1~a7, b1~b3 = cdefgab
# 같은 제목 두번 이상 x



#출력 : 맞힌기를 시도할 노래에 대하여 프로그램에 저장된 노래와 첫 세음이 동일한 노래가 하나만 있따면 해당 노래 제목을,
# 만약 두개 이상 있다면 ?
# 없으면 !

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
song = {}

for _ in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    A = [a1, a2, a3]	# 첫 세 음만 리스트로 저장
    song[S] = A		# key가 노래 제목, value가 첫 세 음

for _ in range(M):
    B = input().split()
    count = 0	# 같은 노래가 몇 개인지 저장할 변수
    title = ""	# 노래 제목 저장할 변수

    for s in song:
        if B == song[s]:	# 첫 세 음이 같다면
            count += 1
            title = s	# title 변수는 count가 1일때만 기능을 발휘한다.

    if count >= 2:
        print("?")
    elif count == 1:
        print(title)
    else:
        print("!")

# 메모리 	31120 KB
# 시간      144 ms