def add (x,y):
    return(x+y)

def sub (x,y):
    return(x-y)

def mult (x,y):
    return(x*y)

def div (x,y):
    return(x/y)

def float( x,y):
    return(x//y)

sum=input("select an operand:")
num_2=int(input("enter a second number:"))
num_1=int(input("enter a first number:"))

if sum=="+":
    print("result",num_1+num_2)
elif sum=="-":
    print("result",num_1-num_2)
elif sum=="*":
    print("result",num_1*num_2)
elif sum=="/":
    print("result",num_1//num_2)
elif sum=="//":
    print("result",num_1//num_2)
else:
    print("invalid operand")
