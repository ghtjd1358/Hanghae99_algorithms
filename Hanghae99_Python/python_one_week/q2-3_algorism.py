#3
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    
    return (w(a - 1, b, c) + w(a - 1, b - 1, c) +
            w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1))

t = int(input())  

for _ in range(t):
    data_input = input()
    x, y, z = map(int, data_input.split())
    print(f"w({x}, {y}, {z}) = {w(x, y, z)}")


def draw(start_x, start_y, size):
    # 크기가 1 이하이면 '*'
    if size <= 1:
        str[start_x][start_y] = '*'
        return

    # 윗줄과 아랫줄에 '*'을 그려줌
    for col in range(start_y, size):
        str[start_x][col] = '*'
        str[size-1][col] = '*'

    # 왼쪽줄과 오른쪽줄에 '*'을 그려줌
    for row in range(start_x, size):
        str[row][start_y] = '*'
        str[row][size-1] = '*'

    # 안쪽 사각형을 그리기 위해 좌표와 크기를 조정해서 다시 호출
    draw(start_x + 2, start_y + 2, size - 2)

def print_str():
    for row in str:
        print(''.join(row))

n = int(input())
length = 1 + (4 * (n - 1))  # 사각형의 크기 계산
str = [[' '] * length for _ in range(length)]  # 공백란

draw(0, 0, length)  # 가장 바깥 사각형
print_str() 




