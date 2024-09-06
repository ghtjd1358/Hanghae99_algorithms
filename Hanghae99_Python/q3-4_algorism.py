    # ==================== 테스트 4 =============================

A, B = input().split()

reverse_A = A[::-1]
reverse_B = B[::-1]

A_nums = int(reverse_A)
B_nums = int(reverse_B)

print(max(A_nums, B_nums))
