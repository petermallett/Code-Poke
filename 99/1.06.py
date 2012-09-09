print "1.06 (*) Find out whether a list is a palindrome."
#A palindrome can be read forward or backward; e.g. [x,a,m,a,x].

def is_palindrome(a):
  b = list(a)
  a.reverse()
  if b == a:
    return True
  else:
    return False

a_list = [1, 2, 3, 4]
print a_list
print is_palindrome(a_list)
a_list = [1, 3, 6, 3, 1]
print a_list
print is_palindrome(a_list)
