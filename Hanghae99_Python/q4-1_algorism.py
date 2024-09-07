N = int(input())
array = list(map(int, input().split()))
result =[]

for i in range(N):
    result.insert(i-array[i], i+1)

print (result)