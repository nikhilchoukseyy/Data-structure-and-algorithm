def solve(): 
  n , h = map(int,input().split())
  arr = []
  for i in range(n): 
    arr.append(list(map(int,input().split())))

  zero_counts = [0]*n
  peak_hours = [0]*h
  total_consumption = 0

  def zeroCounts(nums): 
    count = 0 
    for num in nums : 
      if num == 0 : 
        count += 1

    return count 

  def isStrictlyIncreasing(nums): 
    for i in range(1,len(nums)) : 
      if nums[i] < nums[i-1]: 
        return False 

    return True 

  for i in range(n): 
    zero_counts[i] = zeroCounts(arr[i])
    if zero_counts[i] == 0 and isStrictlyIncreasing(arr[i]): 
      total_consumption += sum(arr[i])

  for a in arr: 
    for i in range(h):  
      peak_hours[i] += a[i]

  peak_hour = 0 
  peak_value = peak_hours[0]

  for i in range(1,len(peak_hours)): 
    if peak_hours[i] > peak_value : 
      peak_value = peak_hours[i]
      peak_hour = i

  return [zero_counts,total_consumption,peak_hour]

result = solve()
print("|".join(map(str,result)))