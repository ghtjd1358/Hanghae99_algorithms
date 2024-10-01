# --------------------------------1번 문제-----------------------------

input_data = input()

A,B = input_data.split()

A = int(A)
B = int(B)

if A > B:
    print('>')
elif B > A:
    print('<')
else:
    print('==')
