# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

# Examples:
# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

# Input: arr[] = [2, 3, 4, 5, 6]
# Output: 0
# Explanation: As the sequence is already sorted so there is no inversion count.

# Input: arr[] = [10, 10, 10]
# Output: 0
# Explanation: As all the elements of array are same, so there is no inversion count.


def countAndMerge(arr,l,m,r): 
  n1 = m-l+1 
  n2 = r-m
  
  left = arr[l:m+1]
  right = arr[m+1:r+1]
  
  res= 0 
  i = 0 
  j = 0 
  k = l 
  
  while i < n1 and j < n2 : 
    if left[i] <= right[j]: 
        arr[k] = left[i]
        i+=1 
    else : 
        arr[k] = right[j]
        j+=1 
        res += (n1-i)
    k+=1 
  
  while i < n1 : 
    arr[k] = left[i]
    k+=1 
    i+=1 
  
  while j < n2 : 
    arr[k] = right[j]
    k+=1 
    j+=1 
  
  return res 

def countInv(arr,l,r): 
  res = 0 
  if l < r : 
    m = l + (r-l)//2

    res += countInv(arr,l,m)
    res += countInv(arr,m+1,r)
    
    res += countAndMerge(arr,l,m,r)
  return res 
      
def inversionCount(arr):
  return countInv(arr,0,len(arr)-1)

if __name__ == "__main__" : 
  arr = [4, 3, 2, 1]
  print(inversionCount(arr))