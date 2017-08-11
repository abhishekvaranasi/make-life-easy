atoz = ([chr(i) for i in range(ord("a"), ord("z")+1)])
name = input()
value = 0
for i in name:
  for v,ch in enumerate(atoz):
    if i == ch:
      value += v+1

print(value)
    
