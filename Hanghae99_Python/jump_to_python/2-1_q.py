# 1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
gildong = {'국어' : 80, '영어' : 75, '수학' : 55}
sum = 0
for value in gildong.values() :
    sum+=value
    results = sum/3

    print(f'평균점수 : {results}')

# 2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 알아보자.
int_value = 13

if int_value % 2 == 0 :
    print('짝수')
else:
    print('홀수')

# 3. 홍길동 씨의 주민 등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일 (YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[-7:-1]
print(yyyymmdd)
print(num)

# 4. 주민번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민번호에서 성별을 나타내는 숫자를 출력하자.
print(pin[7])

# 5. 다음과 같은 문자열 a: b: c: d가 있다. 문자열의 replace 함수를 사용하여 a # b # c # d 로 바꿔서 출력하자
q5 = "a : b : c : d"
print(q5.replace(':', '#'))

# 6. [1 , 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1] 로 출력해보자
q6 = [1 , 3, 5, 4, 2]
q6.sort()
# q6.reverse() <= 이것도 가능
print(list(reversed(q6)))

#7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해보자.
q7 = ['Life', 'is', 'too', 'short']
results7 = ' '.join(q7)
print(results7)

#8. (1 ,2 ,3) 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 출력해보자.
q8 = (1, 2, 3)
q8 = q8 + (4, )
print(q8)

