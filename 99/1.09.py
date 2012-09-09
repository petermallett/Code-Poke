print "1.09 (**) Pack consecutive duplicates of list elements into sublists."
#If a list contains repeated elements they should be placed in separate
#sublists.

def pack(a):
  result = []
  sub_list = []
  for i, x in enumerate(a):
    if i > 0 and x != a[i - 1]:
      result.append(sub_list)
      sub_list = [x]
    else:
      sub_list.append(x)
  result.append(sub_list)

  return result

a_list = [1,1,1,1,2,3,3,1,1,4,5,5,5,5]
print a_list
print pack(a_list)
