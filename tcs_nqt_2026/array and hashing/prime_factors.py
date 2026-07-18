def primeFactors(): 
  n = int(input()) 
  i = 2 
  result = []
  while i*i <= n: 
    if n%i == 0 : 
      n //=i 
      result.append(i)
    else : 
      i += 1 

  if n > 1 : 
    result.append(n)
  return result

print(*primeFactors())