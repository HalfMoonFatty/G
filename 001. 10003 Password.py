import sys
sys.setrecursionlimit(10005)

def find_recursive(code):
  if len(code) == 10003:
    print code
    return True
  for i in range(10):
    if code.find(code[-3:] + str(i)) == -1:
      if find_recursive(code + str(i)):
        return True
  return False
  
find_recursive('000')
