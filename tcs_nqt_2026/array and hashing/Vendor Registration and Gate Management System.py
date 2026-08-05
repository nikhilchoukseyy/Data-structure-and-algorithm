# Problem Statement

# A society maintains a list of registered vendors who are allowed to enter the premises.

# You are given:

# A list of registered vendor IDs.
# A sequence of gate operations.

# The system must process the following operations.

# Operations
# 1. ENTRY X
# If vendor X is registered, allow entry and add the vendor to the list of active vendors.
# Otherwise, count it as a blocked attempt.
# 2. EXIT X
# If vendor X is currently active, remove the vendor from the active vendor list.
# Otherwise, ignore the operation.
# 3. CHECK X
# Count this as a check request.
# The operation only verifies whether vendor X is currently active and does not modify the system.

# After processing all operations, print:

# Number of active vendors.
# Number of blocked entry attempts.
# Number of check requests.
# Input Format
# First line contains an integer N, the number of registered vendors.
# Second line contains N space-separated vendor IDs.
# Third line contains an integer M, the number of operations.
# The next M lines each contain one operation in one of the following formats:
# ENTRY X
# EXIT X
# CHECK X
# Output Format

# Print:

# Active Vendors: X
# Blocked: Y
# Checked: Z

# Where:

# X = Number of active vendors after all operations.
# Y = Number of blocked entry attempts.
# Z = Number of check requests.
# Sample Input
# 2
# 101 102
# 5
# ENTRY 101
# ENTRY 102
# ENTRY 103
# CHECK 105
# EXIT 101
# Sample Output
# Active Vendors: 1
# Blocked: 1
# Checked: 1
# Explanation

# Registered vendors:

# 101 102

# Process each operation:

# Operation	Result
# ENTRY 101	Allowed → Active = {101}
# ENTRY 102	Allowed → Active = {101, 102}
# ENTRY 103	Not registered → Blocked = 1
# CHECK 105	Check request → Checked = 1
# EXIT 101	Remove 101 → Active = {102}

# Final state:

# Active Vendors = 1
# Blocked Attempts = 1
# Check Requests = 1


def solve(): 
	reg_no = int(input())
	reg_ids = set(map(int,input().split()))
	n = int(input())
	active_ids = set()
	blocked = 0 
	checked = 0 
	for i in range(n): 
		operation , vid = input().split()
		vid = int(vid)
		
		if operation == "ENTRY": 
			if vid in reg_ids : 
				active_ids.add(vid)
			else : 
				blocked += 1 
		elif operation == "CHECK":
			checked += 1 
		elif operation == "EXIT":
			active_ids.discard(vid)
	
	print("Active Vendors: ",len(active_ids))
	print("Blocked: ",blocked)
	print("Checked: ",checked)
	

solve()