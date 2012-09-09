print "1.07 (**) Flatten a nested list structure."

def flatten_list(a):
  result = []
  for x in a:
    if type(x) is list:
      result.extend(flatten_list(x))
    else:
      result.append(x)
  return result

a_list = [1, [2, [3, 4], 5], 6]
print a_list
print flatten_list(a_list)
