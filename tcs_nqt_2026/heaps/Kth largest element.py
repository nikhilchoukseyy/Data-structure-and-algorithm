# Question

# Return K largest numbers.

# Example

# 5 2 8 9 1 6

# k=3

# Output

# 9 8 6

import heapq

def solve(): 
  nums = list(map(int,input().split()))
  k = int(input())

  heap = []

  for num in nums : 
    heapq.heappush(heap,num)
    if len(heap) > k : 
      heapq.heappop(heap)

  return sorted(heap,reverse=True)


print(*solve())