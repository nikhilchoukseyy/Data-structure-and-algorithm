# In this question we have to check if any given number is odd or not through bit manipulation 
# if any number is odd then its most significant bit in binary representation will be 1 , like 
# 3 -> 011 , 5 -> 101  
# if we do and operation between given number and 1 then the most significant will be one because 
# 1 -> 001 
# 011 & 001 -> 001 [0&0 == 0,0&1 == 0 , 1&1 == 1]
# result will be one if and only if msb is 1 otherwise 0 



def oddOrNOt(n): 
  return (n & 1 ) == 1 

print(oddOrNOt(412))

