import string

atoz = ([chr(i) for i in range(ord("a"), ord("z")+1)])  #Method 1
ch = list(string.ascii_lower) #Method 2
name = input()
value = 0
for i in name:
  for v,ch in enumerate(atoz):
    if i.lower() == ch:
      value += v+1
print(value)
