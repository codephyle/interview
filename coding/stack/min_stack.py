"""
MIN STACK

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
     MinStack() initializes the stack object.
     void push(int val) pushes the element val onto the stack.
     void pop() removes the element on the top of the stack.
     int top() gets the top element of the stack.
     int getMin() retrieves the minimum element in the stack.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""
# https://leetcode.com/problems/min-stack/solution/

# idea is to maintain one more stack with min element seen so far at the top

class MinStack:

     def __init__(self):
          self.stack = []
          self.mins = []

     def push(self, val):
          self.stack.append(val)
          if not self.mins or self.mins[-1] >= val:
               self.mins.append(val)


     def pop(self):
          if self.stack:
               old = self.stack.pop()
               if self.mins[-1] == old:
                    self.mins.pop()
          
     def top(self):
          return self.stack[-1] if self.stack else None
     
     def getMin(self):
          return self.mins[-1] if self.mins else None