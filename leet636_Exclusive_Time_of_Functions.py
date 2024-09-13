# Solution

# // Time Complexity :  O(length of logs)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Use stack and previous values, also consider if we are having start or end in previous and start or end in current
# https://www.youtube.com/watch?v=e9tAbhSJIuQ

from collections import deque

def exclusiveTime(n, logs):
        result = [0]*n
        stack = deque()
        temp = logs[0].split(":")
        stack.append(int(temp[0]))

        for i in range(1,len(logs)):
            prev = logs[i-1].split(":")
            curr = logs[i].split(":")

            if prev[1] == "start":
                length = int(curr[2]) - int(prev[2])
                result[int(stack[-1])] += length
            elif prev[1] == "end" and len(stack)>0:
                length = int(curr[2]) - int(prev[2]) - 1
                result[int(stack[-1])] += length
            
            if curr[1] == "end":
                result[int(curr[0])] += 1
                stack.pop()
            else:
                stack.append(int(curr[0]))

        return result

if __name__ == "__main__":
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    print(exclusiveTime(n,logs))