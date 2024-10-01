# 1.빈 배열 생성 및 단어 추가
# 2. for문을 돌려 list에 있는 단어들을 빼고 reverse
# 3. words 리스트 안에 reverse 시킨 단어와 동일한 단어가 있으면 참 
# 4. break으로 반복문 

import sys
input = sys.stdin.readline

N = int(input())
words = [] 

for _ in range(N):
    words.append(input().strip()) #Words 리스트 생성 [ "las", "god", "psala",  "sal" ]

for word in words:
    reversed_word = word[::-1]

    if reversed_word in words: # sal이 words 에 있는지 비교 참이면 아래처럼 출력
        center = len(word) // 2
        print(len(word), word[center])  
        break  

# 메모리 	31120 KB
# 시간      32 ms