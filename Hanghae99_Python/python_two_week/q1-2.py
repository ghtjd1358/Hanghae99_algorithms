import sys
from collections import deque

# 시간 초과 문제로 사용
input = sys.stdin.readline

N = int(input())

queue = deque([])

for i in range(N):
    command = input().split()
    
    # command[0]가 문자열 push_front이면 queue에 command[1] 값을 추가 전체적으로 맥락이 비슷하여 아래 설명은 생략 
    if command[0] == "push_front": 
        queue.appendleft(int(command[1]))
    
    elif command[0] == "push_back":
        queue.append(int(command[1]))
    
    elif command[0] == "pop_front":
        if queue:
            print (queue.popleft())
        else:
            print (-1)

    elif command[0] == "pop_back":
        if queue:
            print (queue.pop())
        else:
            print (-1)
    
    elif command[0] == "size":
        print (len(queue))
    
    elif command[0] == "empty":
        if queue:
            print (0)
        else:
            print (1)

    elif command[0] == "front":
        if queue:
            print (queue[0])
        else:
            print (-1)
        
    elif command[0] == "back":
        if queue:
            print (queue[-1])
        else:
            print (-1)