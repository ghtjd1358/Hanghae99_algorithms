# --------------------------------2번 문제-----------------------------

# input_data = input()
# A,B,C,D,E = input_data.split()
# x = [A,B,C,D,E]
# sum = 0

# for xs in x:
#     sum+=int(xs) ** 2

# verification = sum % 10
# print(f"검증수 : {verification}")

# //

input_data = input()
sum = 0
nums = list(map(int, input_data.split()))

sum_list = sum(num ** 2 for num in nums)

verification = sum_list % 10
print(f"검증수 : {verification}")

