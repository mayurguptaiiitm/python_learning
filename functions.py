#declaring a function
def simple():
    print ("My First Function")

#calling the function
simple()

#here function returns the value
def plus_ten(a):
    return a + 10

y = plus_ten(2)
print(y)

#here declaring variable in the body of the function
def add_ten(a):
    result = a + 10
    return result
#remember only single return can be done via a function.
add_ten(10)
print(add_ten(10))

#function within a function

def wage(w_hours):
    return w_hours * 25

def with_bonus(w_hours):
    return wage(w_hours) + 50

print(wage(8), with_bonus(8))

#functions with conditionals 
# Imagine a boy has to save money and if he saves more than 100 then his mom gives him 10 more as reward 
# else he gets nothing 

def savings_report(m):
    if m >= 100:
        m = m + 10
        return m
    else:
        return "Save More!!"

print("If saves amount is 120", savings_report(120))
print("if the saved amount is 10",savings_report(10))

#more than one parameter in a function

def substract_bc(a,b,c):
    result = a - b*c
    print ('Parameter a equals', a)
    print ('Parameter b equals', b)
    print ('Parameter c equals', c)
    return result
#providing the values in order
print(substract_bc(10,3,2))
#specifying manually values if order is not known
print(substract_bc(b=3,a=10,c=2))


#built in functions 
type(10)

int(5.0)

float(3)

str(500)

max(10,20,30)
min(10,20,30)

z = -20
abs(z) #returns absolute value of z

list_1 = [1,2,3,4]
sum(list_1) #returns sum of the numbers in list

round(3.5555,2) # rounds the numbers to the number of digits asked if the digits are not specified it will default to zero

pow(2,10) # pow function is 2 power of 10 

#how many elements are in a object 
len("mayur")


