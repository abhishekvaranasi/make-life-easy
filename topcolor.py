def topColor(img):
  color =dict()

  for i in img:
    for j in i:
      if j in color:
        color[j] += 1
      else:
        color[j] = 1
  
  maximum_value = max(color.values())
  maximum_key = [k for k, v in color.items() if v == maximum_value]
  
  return (",".join(sorted(maximum_key)))

#test case
l = [["red","green","red"], ["yellow", "red", "yellow"], ["green","green", "yellow"]]
print(topColor(l))