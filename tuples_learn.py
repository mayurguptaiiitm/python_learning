# Tuples are a type of data sequences 
# tuples are immutable  you cannot append or delete the elements 

x = (40,41,42) # () denotes declaration of the tuples. all 3 values are packed into a tuple.

x[0] # will give 40 

# this is basically assiging the values 30 to age and 17 to years_of_school 
# where split is comma seperated values
(age,years_of_school) = "30,17".split(',') 

#functions can return tuples as values

def square_info(x):
    A = x ** 2
    P = 4 * x
    print("Area and Perimeter:")
    return A,P

print(square_info(3))
