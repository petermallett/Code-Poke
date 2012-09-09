print "1.08 (**) Eliminate consecutive duplicates of list elements."
#If a list contains repeated elements they should be replaced with a single
#copy of the element. The order of the elements should not be changed.

def compress(a):
  result = [a[0]]
  current = a[0]
  for x in a:
      if x != current:
        result.append(x)
      current = x

  return result

a_list = [1,1,1,1,2,3,3,1,1,4,5,5,5,5]
print a_list
print compress(a_list)
