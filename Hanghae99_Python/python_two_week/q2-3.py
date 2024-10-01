#문제에서 지시한대로만 풀 면 될 것 같다.

import sys
input = sys.stdin.readline

#의식의 흐름으로 int로 감싸며 시간이 길어졌다.
N = input().strip()  # 입력값 공백 제거
count = 0 

# 각 자리수의 합이 한 자리 숫자가 될 때까지 반복
while int(N) >= 10:
    str_sum = 0
    for i in range(len(N)):
        str_sum += int(N[i])
    N = str(str_sum)
    count += 1 

print(count)

# 3의 배수인지 판단
if int(N) % 3 == 0:
    print("YES")
else:
    print("NO")
