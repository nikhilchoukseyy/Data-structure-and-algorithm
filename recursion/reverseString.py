def reverseString(str,idx): 
  if idx >= len(str): 
    return 
  
  reverseString(str,idx+1)
  print(str[idx])
  
reverseString("Nikhil",0)