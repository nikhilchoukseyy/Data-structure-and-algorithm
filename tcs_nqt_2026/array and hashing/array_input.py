# If all numbers are on the same line
# Input:
# 5
# 7 4 8 2 9

#code 
N = int(input()) # size
A = list(map(int,input().split()))

#------------------------------------------------
# 2. If each number is on a new line
# Input:
# 5
# 7
# 4
# 8
# 2
# 9

#code
N = int(input())
A = [int(input()) for _ in range(N)]


#-----------------------------------------------
# If N and the array are on the same line
# Input:
# 5 7 4 8 2 9

data = list(map(int,input().split()))
N = data[0]
A = data[1:]

