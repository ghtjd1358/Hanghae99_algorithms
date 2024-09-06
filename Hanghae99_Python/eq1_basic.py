from math import isclose
from decimal import Decimal

# 연산자
print("use round function", round(0.1 + 0.1 + 0.1, 1) == 0.3 )
print("use isclose function :", isclose(0.1 + 0.1 + 0.1, 0.3))
# Deciaml은 float으로 값을 전달하면 오차가 있는 시점으로 값을 더하기 때문에 주의해야함
print("decimal module: ", Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')) 

# Boolean Type

# 예약어
x = True 
y = False

# 불린 타입도 연산자가 존재
print(True and True) # and 연산자는 둘 다 True일때만 True 값을 반환, and 연산자의 좌항이 false 이면 무슨 값이 들어오든 false 하지만 좌항이 true이면 false일 수도 true일 수도 있기 때문에 좌항이 true이면 우황 값을 반환
print(False or False) # or 연산자는 둘 다 False 일때만 false 값을 반환, or 연산자의 경우 좌항이 True이면 무슨 값이 들어오던 true 이기 때문에 바로 좌항 값을 반환한다, 반대로 좌항의 값이 False 이면 우황에 값에 따라 결과가 갈리기 때문에 우황 값을 반환

# True and 'Python'
print("Python" or True) 
# or연산자
# 좌항이 truthy인 경우: or 연산자는 좌항의 값을 반환 
# 좌항이 falsy인 경우: or 연산자는 우항의 값을 반환

# and 연산자
# 좌항이 falsy인 경우: and 연산자는 좌항의 값을 반환
# 좌항이 truthy인 경우: and 연산자는 우항의 값을 반환


#index
a = 'hello'
print('인덱싱', a[2])
print('슬라이싱', a[0:4:2])
print(a[2::-1])
#indexing => 하나를 집어서 가져옴

#slicing => 여러개를 집어서 가져옴 [ 시작 : 끝 : 스텝 ] => 스텝 값을 적지 않으면 default 값은 1

# 조건문

