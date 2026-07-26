#there r several ways to take multiple inputs from a user in python
# CASE 1: n1,n2,n3 =int(input("Enter three numbers seperated by spaces: ")).split()

# CASE 2: n  =list(map(int, input("enter three numbers seperated by spaces: ").split()))

# CASE 3: num1,num2,num3,num4 = map(int, input("Enter four numbers separated by spaces : ").split())

#actually this is also a way of taking inputs from a user inpython but it was normal......
#n  = int(input())
#n1 = int(input())
#n2 = int(input())



#PROGRAM IS DEMO OF ELIF CLAUSE.... FINDING GREATEST AMONG 4 NUMBERS
n1,n2,n3,n4 = map(int, input("Enter four numbers separated by spaces: ").split())
if n1>n2 and n1>n3 and n1>n4:
    print(n1,"is the greatest number")
elif n2>n1 and n2>n3 and n2>n4:
    print(n2,"is the greatest number") 
elif n3>n1 and n3>n2 and n3>n4:
    print(n3,"is the greatest number")
else:
    print(n4,"is the greatest number")



