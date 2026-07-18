# ◇
# Problem Statement
# Before the coronavirus outbreak, a meeting took place where everyone shook hands with everyone else exactly once. Given N people in the room, find the total number of handshakes.

# Constraints:
# - Values fit in signed 64-bit integers unless stated otherwise.
#    - Input is assumed valid unless the problem explicitly asks for validation.
#    - Use O(N) or better whenever a direct traversal solution exists.

# I/O format:
# - Input: The integer values described in the question.
# - Output: The computed answer.
# ◇
# Complexity
# Time
# O(1) or O(N)
# Space
# O(1)
# Math / combinatorics formula.

# ◇
# Examples & Test Cases
# Dry-run these inputs before reading the solution — each shows why the output is correct.

# Example 1
# Input
# 5
# Output
# 10
# Why this output? 5 people → each shakes 4 others → 5×4/2 = 10 unique handshakes.

# Example 2
# Input
# 3
# Output
# 3
# Why this output? 3 people → 3×2/2 = 3 handshakes (triangle).


N = int(input())
print(int(N*(N-1)/2))