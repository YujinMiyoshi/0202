import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    class info:
      def __init__(self, number, string):
        self.number = number
        self.string = string
      
    #numbers = []
    #strings = []
    ans = [0]
    answer = ""
    lines = lines.split()
    informations = {i: info(False, False) for i in range(len(lines) - 1)}
    
    for i, v in enumerate(lines):
      val = v.split(":")
      val[0] = int(val[0])
      if len(val) != 1:
        #numbers.append(val[0])
        #strings.append(val[1])
        informations[i].number = val[0]
        informations[i].string = val[1]
        
      else:
        num = val[0]
    """
    for i, n in enumerate(numbers):
      if num % n == 0:
        ans.append(strings[i])
    """   
    for i in range(len(lines) - 1):
      #print(i, informations[i].number, informations[i].string)
      if num % informations[i].number == 0:
        ans.append(informations[i].string)
    #print(ans)   
    if len(ans) == 1:
      print(num)
        
    for i in ans[1:]:
      answer += i
      
    print(answer)

if __name__ == '__main__':
    lines = []
    """
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    """
    l = sys.stdin.readline()
    main(l)