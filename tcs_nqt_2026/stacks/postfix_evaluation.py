def postfix_evaluation(): 
  expression = input()
  stack = []
  for data in expression : 
    if data.isdigit(): 
      stack.append(int(data))
    else :
      operand2 = stack.pop() 
      operand1 = stack.pop()
      if data == "+": 
        stack.append(operand1+operand2)
      elif data == "-": 
        stack.append(operand1-operand2)
      elif data == "*": 
        stack.append(operand1*operand2)
      elif data == "/": 
        stack.append(operand1//operand2)
  return stack.pop()

print(postfix_evaluation())