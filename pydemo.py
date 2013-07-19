import os
import sys


class pydemo:
  def __init__(self):
    self.msg = 'Hello GitHub~~'
    
  def start(self):
    self.printMsg()
    
  def printMsg(self):
    print(self.msg)
    
    
    
if __name__ == '__main__':
  op = pydemo()
  op.start()
