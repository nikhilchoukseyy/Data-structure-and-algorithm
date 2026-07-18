def compare_price(): 
  A,B = list(map(int,input().split()))

  if A == 0 or B == 0 : 
    return "Invalid input"
  elif A == B : 
    return "Prices equal"
  elif A > B : 
    return f"{A} is more expensive"
  else : 
    return f"{B} is more expensive"
  
print(compare_price())