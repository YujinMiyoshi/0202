import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    numbers = []
    strings = []
    lines = list(*lines)
    #print(lines)
    for v in lines:
      num = ""
      s = ""
      if(v in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        num += v
        num_n = int(num)
        print(num_n)
        numbers.append(num_n)
      elif(v in "abcdefghijklmnopqrstuvwxyz"):
        s += v
        print(s)
        strings.append(s)
        
      for num
  

        
        
        
    #print(f"line[{i}]: {v}")
    print(numbers, strings)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
    
"""
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
  """