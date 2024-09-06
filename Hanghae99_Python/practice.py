# data_input = input()

# data_array = data_input.split()

# N = int(data_array[0])
# M = int(data_array[1])

# hot_Bread = []

# for x in range(N):
#     data = input()
#     hot_Bread.append(data)

# for data in hot_Bread:
#     reversed = data[::-1]
#     print(reversed)

# 

n= int(input())

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))

# def fibonachi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)
    
# print(fibonachi(n))