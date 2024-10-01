import sys

input = sys.stdin.readline
N = int(input())
stack = []

# 1. list 생성
# 2. input 값 생성
# 3. AA, BB 가 있으면 좋은단어, A들어가고 B 들어가면 나쁜단어, list[-1] 값과 배열에 들어갈 값이 다르면 안좋은 단어 , 즉 list에 아무것도 없는 것이 핵심
# 4. 좋은 단어만 카운트하고

for _ in range(N):
    text = input().rstrip()
    count = N

    for s in text:
        if not stack:
            stack.append(s)
        elif stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    if stack:
        count -= 1

print(count)
        


