# ----------------------------- 테스트 1
N = int(input())

for _ in range(N):
    R, S = input().split()
    R = int(R)
    result = ''.join([j * R for j in S])
    print(result)
