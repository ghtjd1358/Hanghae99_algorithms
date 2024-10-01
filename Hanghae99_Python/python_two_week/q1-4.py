while True:
  str = input()
  stack = []
  results = 'yes'

  if str == '.':
    break
  
  for s in str:
    if s=='(' or s=='[': #열린 괄호가 들어오면 stack 배열에 추가
      stack.append(s)
    elif s == ')':
      if not stack: # '(' 괄호가 나오기 전에 ')' 괄호가 나온 경우
        results = 'no'
        break
      else:
        if stack.pop() != '(': # 제외한 괄호가 '(' 아닌 경우
          results = 'no'
          break
    elif s == ']':
      if not stack: 
        results = 'no'
        break
      else:
        if stack.pop() != '[':
          results = 'no'
          break
    else:
      continue
    
  if stack:
    results = 'no'
  print(results)


  #여기 코드에서 sys 사용하면 출려초과 뜸