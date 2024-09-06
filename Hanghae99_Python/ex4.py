# data_input = input()
# data_list = list(map(int, data_input.split()))
# data_lamda = list(map(lambda x: x * 2, data_list))

# print(data_lamda)



# print(type(data_input))

# print('0', data_list[0]* 5)
# print('1', data_list[1]* 5)

# print(type(data_list[0]))
# print(type(data_list))

# print(len(data_list))
# print(min(data_lamda), max(data_lamda), sum(data_lamda))

# list1 = [1,2,3,4]
# list2 = ['A', 'B', 'C', 'D']

# print(list(zip(list1, list2)))
# print(list(reversed(data_lamda)))

# 
# n = int(input())
# list_of_list = []

# for m in range(n - 1):
#     m = input()
#     array = list(map(int, m.split()))
#     list_of_list.append(array)
#     last_revese = list(reversed(list_of_list))

# print(last_revese)

data_input = input()
data_array = list(map(int, data_input.split()))

data_sort = list(sorted(data_array))
print(data_sort)

