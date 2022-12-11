#Lists in python
"""
This might not be a multiline comment but it can be used as such. appears this is how a long string can
be attached to a variable to store the value
"""

sample_list = ['abc','def','efg','ijk']

sample_list[3]
#do not use () or {}
#accessing the list by indexing the value 3

sample_list[-1]
#reverse traverse here the numbers start with -1 

#replacing or deleting item in list 
sample_list[3] = 'Maria'

del sample_list[2]
#del is used to delete the vaule for the index and so the length or index changes.

#using method : syntax is after name of the object put a (dot) . and then tha name of method
sample_list.append("Mayur")

#same can be done using extend

sample_list.extend(['smriti','biwi'])

#list elements are directly treated as string values
#len() counts the elements in the object


#slicing a list 
# first number is the first position of interest and then last is the number where it needs to end
#this way the list is split or mainly new is extracted
sample_list[1:3]
sample_list[:2]
#this :2 gives the first 2 since it takes 0 as the first
sample_list[4:]
# 4: basically everything after 4
#same can be done with the negetive numbers 
# [-2:] gives the same output as before

#finding the location of a value in the list 
sample_list.index("Mayur")

newlist  = ['hello','world']

bigger_list = [sample_list,newlist]

#.sort() method basically sorts the values either in the alphabetical or numerical based on the type of values
#.sort(reverse=True) does the same just in reverse
