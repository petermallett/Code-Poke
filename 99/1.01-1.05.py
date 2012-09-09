print "1.01 (*) Find the last element of a list."
a_list = [1, 2, 3]
print "a_list = " + str(a_list)
print a_list[-1]

print "1.02 (*) Find the last but one element of a list."
print a_list[-2]

print "1.03 (*) Find the K'th element of a list."
K = 3
a_list = [1, 2, 3, 4, 5, 6]
print "K = " + str(K)
print "a_list = " + str(a_list)
print a_list[K - 1]

print "1.04 (*) Find the number of elements of a list."
print len(a_list)

print "1.05 (*) Reverse a list."
a_list.reverse()
print a_list
