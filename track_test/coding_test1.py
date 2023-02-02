import sys

def main(lines):
    class info:
      def __init__(self, number, string):
        self.number = number
        self.string = string
        
      def calc(self):
        if num % self.number == 0:
          ans.append(self.string)
          
      def print_ans(self, answer):
        if len(ans) == 1:
          print(num)
        
        for i in ans[1:]:
          answer += i
      
        print(answer)
   
    ans = [0]
    answer = ""
    lines = lines.split()
    informations = {i: info(False, False) for i in range(len(lines) - 1)}
    
    for i, v in enumerate(lines):
      val = v.split(":")
      val[0] = int(val[0])
      if len(val) != 1:
        informations[i].number = val[0]
        informations[i].string = val[1]
        
      else:
        num = val[0]
  
    for i in range(len(lines) - 1):
      informations[i].calc()
   
    informations[0].print_ans(answer)

if __name__ == '__main__':
    lines = []
    l = sys.stdin.readline()
    main(l)