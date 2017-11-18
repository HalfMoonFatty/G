DIRECTIONS = [[0, 1], [-1, 0], [0, -1], [1, 0]]

  0
1   3
  2
  
class Roomba(object):
  
  def __init__(self, room, x, y):
    self.direction = 0
    self.room = room
    self.x = x
    self.y = y
    self.cleaned = []
  
  def move():
  
  def trun_left():
    
  def turn_right():
    
  def clean():
 
  
  def clean_room(self):
    visited = []
    self.explore(visited, self.x, self.y)
  
  def explore(self, visited, nx, ny):
    if (x, y) in visited:
      return
    self.clean()
    visited.append((x,y))
    for i in range(4):
      self.turn_left(i)
      if self.move():
        self.turn_right(i)
        self.explore(visited, x+DIRECTIONS[i][0], y+DIRECTIONS[i][1])
        
        self.turn_left((i+2)%4)
        self.move()
        self.turn_right((i+2)%4)
      else:
        self.turn_right(i)
        
