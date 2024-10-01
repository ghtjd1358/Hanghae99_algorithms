# --------------------------------3번 문제-----------------------------

n = int(input())

for st in range(1, n + 1):
    print('*' * st + ' ' * (2 * (n - st)) + '*' * st)

for st in range(n - 1, 0, -1):
    print('*' * st + ' ' * (2 * (n - st)) + '*' * st)


# 어려웠다.
data_input = input()
x = int(data_input) 

for st in range(1, x+1):
    stars = '*' * st               
    spaces = ' ' * (2 * (x - st))       
    r_stars = '*' * st              
    print(stars + spaces + r_stars)  

for st in range(x - 1, 1, -1):
    stars = '*' * st              
    spaces = ' ' * (2 * (x - st))       
    r_stars = '*' * st             
    print(stars + spaces + r_stars)  

