# n = int(input())

# card = {
#     'STRAWBERRY' : 0,
#     'BANANA' : 0,
#     'LIME' : 0,
#     'PLUM' : 0,
# }

# for _ in range(n):
#     S, R = input().split()
#     R = int(R)
#     card[S]+=R
#     print(card)    

# if 5 in card.values():
#     print('Yes')
# else:
#     print('No')    

# 3일차 2번

A = list(input().split())  
B = input().strip() 
cnt = 0  


for i in A:
    if i != B and i[:len(B)] == B:
        cnt += 1 
print(cnt)





