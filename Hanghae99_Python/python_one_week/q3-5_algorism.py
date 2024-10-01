# ================== 테스트 5 ============================='

N = int(input())

dicts = {}

for _ in range(N):
    data = input()
    _, extension = data.split('.')
    
    if extension in dicts :
        dicts[extension] += 1
    else:
        dicts[extension] = 1

sorted_dicts = sorted(dicts.items())

for key, value in sorted_dicts:
    print(f"{key},{value}")
    