# a = int(input())

# if a < 3:  
#     print("a는 3미만입니다.")
# else :
#     print("a는 3이상입니다.")


# score = int(85)

# if score >= 60 and score < 70:
#     print("D")
# elif score >= 70 and score <80:
#     print("C")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 90:
#     print('A')

n = 3
s = "Hello"
arr = [1, 2, 3]



# # 문자열 for 문 순회: 문자열 s의 문자를 하나씩 출력하기
# for c in s:
#     print(c)

    # range 함수를 사용해서 0 부터 n-1 을 출력하기
# for i in range(2, 10, 1): 
#     print(i)

# # 리스트 for 문 순회: 리스트 arr의 원소를 하나씩 출력하기
# for x in arr:
#     print(x)

s = "hello"

for c in s :
    if c == "e":
        continue
    print(c)

for c in s :
    if c == "e":
        break
    print(c)

# 
my_dic = {}
my_dic["key"] = "vlaue"

print(my_dic["key"])

mapper = {1: "one", 2: "two", 3: "three"}

for key in mapper.keys():
    print(key, mapper[key])

for value in mapper.values():
    print(value)

for key, value in mapper.items():
    print('item', key, value)

print(mapper.get(4, "No Results@"))


# 3
input_data = input()
x, y, w, h = map(int, input_data.split())

left = x
right = w - x
top = h - y
bottom = y

min_value = min(left, right, top, bottom)

# if min_value > right:
#     min_value = right
# if min_value > top:
#     min_value = top
# if min_value > bottom:
#     min_value = bottom

print(x, y, w, h)

