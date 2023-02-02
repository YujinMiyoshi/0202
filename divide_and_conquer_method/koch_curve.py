import math

rad = math.radians(60)
cos = math.cos(rad)
sin = math.sin(rad)

class point():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
def koch_curve(a, b, n):
  if n == 0:
    return
  
  s = point((2*a.x + b.x)/3, (2*a.y + b.y)/3)
  t = point((a.x + 2*b.x)/3, (a.y + 2*b.y)/3)
  u = point((t.x - s.x)*cos - (t.y- s.y)*sin + s.x, (t.x - s.x)*sin + (t.y - s.y)*cos + s.y)
  
  koch_curve(a, s, n - 1)
  print(f'{s.x:.08f} {s.y:.08f}')
  
  koch_curve(s, u, n - 1)
  print(f'{u.x:.08f} {u.y:.08f}')
  
  koch_curve(u, t, n - 1)
  print(f'{t.x:.08f} {t.y:.08f}')
  
  koch_curve(t, b, n - 1)
  
n = int(input())

a = point(0, 0)
b = point(100, 0)

print(f'{a.x:.08f} {a.y:.08f}')
koch_curve(a, b, n)
print(f'{b.x:.08f} {b.y:.08f}')