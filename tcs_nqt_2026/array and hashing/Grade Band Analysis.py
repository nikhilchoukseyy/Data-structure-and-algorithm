# Problem Statement

# A teacher assigns grades to students based on their marks using the following grading system:

# Marks Range	Grade
# 90 – 100	A
# 80 – 89	B
# 70 – 79	C
# 60 – 69	D
# 50 – 59	E
# 0 – 49	F
# < 0 or > 100	X (Invalid Marks)

# Your task is to:

# Count the number of students in each grade band.
# Print the grade band having the maximum number of students.
# If all students have invalid marks, print X.
# If multiple grade bands have the same maximum count, print the higher-priority grade according to the following priority:
# A > B > C > D > E > F > X
# Input Format
# The first line contains an integer N — the number of students.
# The second line contains N space-separated integers representing the marks obtained by the students.
# Output Format

# Print the grade band having the maximum number of students.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ Marks ≤ 10^9
# Sample Input 1
# 7
# 95 87 92 45 55 78 82
# Sample Output 1
# A
# Explanation

# Grade assigned to each student:

# 95 → A
# 87 → B
# 92 → A
# 45 → F
# 55 → E
# 78 → C
# 82 → B

# Band counts:

# A = 2
# B = 2
# C = 1
# D = 0
# E = 1
# F = 1
# X = 0

# Both A and B have the maximum count of 2.

# According to the priority:

# A > B

# So the output is:

# A
# Sample Input 2
# 5
# -5 130 -8 101 150
# Sample Output 2
# X
# Explanation

# All marks are invalid.

# X = 5

# Since every student has invalid marks, the output is:

# X

def solve(): 
  n = int(input())
  marks = list(map(int,input().split()))
  marks_dict  = {'A':0 , 'B':0 , 'C':0 , 'D':0 , 'E':0 , 'F':0 , 'X':0}

  for mark in marks : 
    if 0 <= mark <=49 : 
      marks_dict['F'] += 1 
    elif 50 <= mark <=59 : 
      marks_dict['E'] += 1
    elif 60 <= mark <=69 : 
      marks_dict['D'] += 1
    elif 70 <= mark <=79 : 
      marks_dict['C'] += 1
    elif 80 <= mark <=89 : 
      marks_dict['B'] += 1
    elif 90 <= mark <=100 : 
      marks_dict['A'] += 1
    else : 
      marks_dict['X'] += 1

  if n == marks_dict['X']: 
    return 'X'
  valid = ['A', 'B', 'C', 'D', 'E', 'F']
  return max(valid, key=lambda g: marks_dict[g])


print(solve())
