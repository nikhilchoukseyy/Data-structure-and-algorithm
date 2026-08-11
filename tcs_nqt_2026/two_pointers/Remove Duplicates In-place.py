# Problem

# Given a sorted array.

# Remove duplicates without using another array.

# Print

# new_length
# modified_array
# Input
# 10
# 1 1 2 2 2 3 4 4 5 5
# Output
# 5
# 1 2 3 4 5

# Hard Test

# 15
# 1 1 1 2 2 3 3 4 5 5 5 6 7 7 8

# Output

# 8
# 1 2 3 4 5 6 7 8

def solve(): 
	n = int(input())
	nums = list(map(int,input().split()))
	i = 0 
	for j in range(len(nums)): 
		if nums[i] != nums[j] : 
			i+= 1 
			nums[i],nums[j]= nums[j],nums[i] 
	return i+1,nums


new_n,new_arr = solve()
print(new_n) 
print(*new_arr[:new_n])