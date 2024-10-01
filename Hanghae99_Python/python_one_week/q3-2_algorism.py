
# ----------------------------- 테스트 2

N = int(input())

fruit_array = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0
} 

for _ in range(N):
    S, R = input().split()
    R = int(R) 
    fruit_array[S]+=R

if 5 in fruit_array.values():
    print("Yes")
else:
    print("No")
