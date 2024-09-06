# 첫 번째 줄에서 N과 M을 입력받습니다.
data_input = input("행의 수와 열의 수를 입력하세요 (N M): ")
data_list = data_input.split() 

N = int(data_list[0])  # 행의 수
M = int(data_list[1])  # 열의 수

# 빈 리스트를 만들어 붕어빵 모양을 저장합니다.
bun_list = []

# N개의 줄에 걸쳐 붕어빵 모양을 입력받아 리스트에 추가합니다.
for i in range(N):
    data = input("붕어빵 모양을 입력하세요: ")  # 한 줄씩 입력받습니다.
    bun_list.append(data)  # 입력받은 줄을 리스트에 추가합니다.

# 리스트의 각 줄을 뒤집어서 출력합니다.
for data in bun_list:
    reversed_data = data[::-1]  # 각 줄을 뒤집습니다.
    print(reversed_data)  # 뒤집힌 줄을 출력합니다.
