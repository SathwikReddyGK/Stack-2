# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Use stack and keep track of open bracket, pop when respective close bracket comes up
# https://www.youtube.com/watch?v=e9tAbhSJIuQ

def isValid(s):
    charList = []
    for char in s:
        if char == "(":
            charList.append(")")
        elif char == "{":
            charList.append("}")
        elif char == "[":
            charList.append("]")
        elif not charList or charList.pop() != char:
            return False
    
    if charList:
        return False
    else:
        return True

if __name__ == "__main__":
    s = "([])"
    print(isValid(s))