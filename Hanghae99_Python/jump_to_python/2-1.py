# a = input().split()
# b = "안녕하세요"

# a_filter = list(filter(lambda x: b not in x, a))  # 필터 결과를 리스트로 변환

# as_filter = filter(lambda x: b not in x, a)  # 필터 객체 생성

# # 반복문을 통해 필터 객체의 값들을 하나씩 출력
# for as_filters2 in as_filter:
#     print(f'as: {as_filters2}')

# # 리스트로 변환된 필터 결과 출력
# print(f'a: {a_filter}')
# print(f'a 타입 : {type(a)}')

# y= 3.46845184
# print(f'{y:0.4f}')

# strings = " ho.  Bby "
# print(f'카운트 : {strings.count("s")}')
# print(f'파인드 : {strings.find("b")}')
# print(f'인덱스 : {strings.index("b")}')
# print(f'조인 : {','.join(strings)}')
# print(f'로우어 : {strings.lower()}')
# print(f'어퍼 : {strings.upper()}')
# print(f'스트립 : {strings.strip()}')
# print(f'리플레이스 : {strings.replace('Bby', 'seong')}')
# print(f'스플릿 : {strings.split()}')
# print(f'스플릿 : {strings.split('.')}')

# =========================== 리스트 ==================================
a_lists = [1, 2, 3, ['a', 'b', 'c']]
print(f'{a_lists[3]}')
print(f'{list(reversed(a_lists[-1]))}')
print(a_lists[3][0:2])

A_prac1 = [1, 2, 3, 4,5]
print(A_prac1[1:3])
# print(A_prac1[0] + 'hi') 에러가 생긴다 그러므로 이유는 정수와 문자는 더 할 수가 없다 아래처럼 바꿔야함
print(str(A_prac1[0]) + 'hi')
A_prac1.insert(2, 5) #리턴값을 반환하고 출력해야함
print(A_prac1)

# =========================== 튜플 ==================================
# 튜플은 list랑 내용물을 수정하거나 삭제할 수 없음
t1 = (1, 2, 3)
t2 = (4, 5)

print(t1[0])
print(t1[1:])
print(t1 + t2) # 튜블은 변형되지 않치만 가능한 이유는 튜플끼리 더하면 새로운 t3라는 메모리주소가 생기고 거기에 t1, t2를 대입하여 새로운 튜플에 생성되어 가능하다고 할 수 있다. 
print(t1 * 2)
print(len(t1))

#======================== 딕셔너리 ===============================
dic = { 'name' : 'hoseong', 'age' : 30, 'freinds' : [1 , 2, 3]}
print(dic['name']) # 이거랑 같은 기능이 get은 None을 반환하지만 반대로 옆처럼 사용하는 경우 error를 반환
dic['ice'] = 'cream'
print(dic)
del dic['ice']
print(dic)

print(dic.keys())
print(list(dic.keys()))
print(dic.values())
print(dic.items())
print('name' in dic)
    
dic.clear()
print(dic)
# for key in dic.keys():
#     print(f'키 값 추출 : {key}')

# for value in dic.values():
#     print(f'밸류 값 적출{value}')

# for key, value in dic.items():
#     print(f'키값, 밸류값 : {key} : {value}')

# ================== 집합자료(set) ========================
# 특징 : 순서가 없고 중복을 허용하지 않는다. 핵심은 교집합, 합집합, 차집합을 구할 때이다.

s = set([1 ,2 ,3,4,5])
print(s)
l = list(s) # tuple도 가능하다
print(l)

s1 = set([1 ,2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))

# 집합 자료형 관련 함수

s3 = set([1, 2, 3])
s3.add(4) # 하나으 값만 추가 가능
print(s3)
s3.update([4, 5, 6]) # 다수의 값을 추가할 때
print(s3)
s3.remove(2)
print(s3)

# boolean 간단하게 활용법만
a = [1, 2, 4, 5]
while a: # 간단학 a가 참일동안 pop을 계속 수행한다. if True : <= 랑 같음
    a.pop()
    print(a)
    print(bool(['python'])) #애매하면 불 연산을 사용하자
    print(bool([])) #애매하면 불 연산을 사용하자


# 변수

[a, b ] =('python', 'life')
print(a)
print(b)


