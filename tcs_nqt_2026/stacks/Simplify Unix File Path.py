# Problem

# Given an absolute Unix path, simplify it.

# Rules

# "." → current directory
# ".." → go back
# multiple "/" ignored
# Input
# /a/./b/../../c/
# Output
# /c

# Example 2

# Input
# /home//foo/

# Output
# /home/foo


def solve(): 
  path = input().split("/")
  stack = []
  for p in path : 
    if p == "" or p == ".": 
      continue
    elif p == "..": 
      if stack : stack.pop()
    else : 
      stack.append(p)

  return "/" + "/".join(stack)

print(solve())
