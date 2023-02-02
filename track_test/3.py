import sys
"""
class person:
  def __init__(self, next, age):
    self.next = next
    self.age = age
"""
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    class person:
      def __init__(self, id, next, min_age):
        self.id = id
        self.next = next
        self.min_age = min_age
    
    age_sum = 0
    
    lines = lines.split('\n')
    #persons = {id: person(False, False, False) for id in range(len(lines))}
    for i, v in enumerate(lines):
      val = v.split()
      #print(val)
      if i == 0:
        n = int(val[0])
        q = int(val[1])
        persons = {id: person(False, False) for id in range(n + 1)}
        
      elif val == []:
        continue
      
      else:
        persons[int(val[0])].id = int(val[0])
        persons[int(val[0])].next = int(val[1])
        #persons[int(val[0])].age = int(val[2])
        pre_age = persons[persons[int(val[0])].next].min_age
        persons[persons[int(val[0])].next].min_age += int(val[2])
        
        if pre_age < persons[persons[int(val[0])].next].min_age:
          print(-1)
          return
      #print(i, persons[i].next, persons[i].age)
        
    for id in range(1, n + 1):
      age_sum += persons[id].min_age
      #print(id, persons[id].min_age)

      
    if age_sum < 0 or 100 < age_sum:
      print(-1)
    
    

if __name__ == '__main__':
    lines = []
    """
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    """
    l = sys.stdin.read()
    main(l)