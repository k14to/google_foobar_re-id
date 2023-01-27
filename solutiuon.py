def solution(i):
  s = "2357111317192329"
  q = 0
  w = 0
  c = len(s) - i
  if c >= 5:
    for x in range(5):
      print(s[i+x],end="")
  if i >= (len(s)-4):
    for x in range(c):
      print(s[i+x],end="")
    for y in range(5-c):
      print(s[q+y],end="") 

  if i == (len(s)):
    for z in range(5):
      print(s[w+z],end="")
