# given two number 

# a = 5 
# b = 6 

# swap both of them using bit manipulation 

# a^a = 0 
# a^0 = a 

# put a = a^b 
# put b = a^b
#       = (a^b)^b
#       = a^b^b 
#       = a [b^b == 0 ]


def swapTwoNum(a,b): 
  a = a ^ b 
  b = a ^ b 
  a = b ^ a 
  
  return " a : " , a  ,  " b : " , b 

print(swapTwoNum(a=5,b=3))