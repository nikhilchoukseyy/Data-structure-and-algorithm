# Input
# nums = [5,1,9,2,7]
# Output
# 1
# 2
# 5
# 7
# 9

# (Hint: Use heapify once, then repeatedly heappop.)

import heapq 

def heap_sort(): 
  nums = list(map(int,input().split()))
  heap = []
  for num in nums : 
    heapq.heappush(heap,num)

  while heap : 
    print(heapq.heappop(heap))
    
heap_sort()

