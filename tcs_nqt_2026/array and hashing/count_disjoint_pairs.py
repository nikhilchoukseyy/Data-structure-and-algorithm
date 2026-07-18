# ### Problem Statement (TCS Style)

# Given an array of `N` integers and an integer `K`, find the **maximum number of disjoint pairs** such that:

# * The sum of each pair is divisible by `K`.
# * Each element can be used **at most once**.

# Return the maximum number of valid pairs that can be formed.

# **Example:**

# ```text
# Input:
# N = 5
# arr = [3, 7, 13, -3, 5]
# K = 10

# Output:
# 2
# ```

# **Explanation:** Valid pairs are `(3, 7)` and `(13, -3)`. The element `5` remains unused.

def countPairs(): 
  nums = list(map(int,input().split()))
  T = int(input())

  freq = {}
  pairs = 0
  for num in nums : 
    r = num%T 
    need = (T-r)%T 
    if freq.get(need,0) > 0 : 
      pairs += 1
      freq[need] -= 1 
    else : 
      freq[r] = freq.get(r,0) + 1
    
  return pairs 

print(countPairs())