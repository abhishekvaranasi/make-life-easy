def binary(l,x):
  start = 0
  end = len(l)-1
  while (start<=end):
    mid = l[int((start+end)/2)]
    if x==mid:
      return x
    elif x<mid:
      end = l.index(mid)-1
    else:
      start = l.index(mid)+1
  return "Not found"  

print(binary([1,2,3,4,5,6,7],6))
