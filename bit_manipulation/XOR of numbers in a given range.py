#find xor from l to r 
# l = 3 
# r = 5 
# result = 3^4^5

def findRangeXor(l,r): 
  result = 0 
  for i in range(l,r+1): 
    result ^= i
  return result

print(findRangeXor(3,5))