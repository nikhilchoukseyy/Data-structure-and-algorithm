def balancedParantheses(): 
  string = input()
  stack = []
  pairs = {
    ")":"(",
    "}":"{",
    "]":"["
  }
  for ch in string : 
    if ch in "({[": 
      stack.append(ch)
    else : 
      if not stack : 
        return print("Not Balanced")
      
      if stack[-1] != pairs[ch]: 
        return print("Not Balanced")
      stack.pop()  
  
  if stack : 
    return print("Not Balanced")
  
  print("Balanced")


balancedParantheses()