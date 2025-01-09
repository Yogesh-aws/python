print("enter 1 for addition")
print("enter 2 for subration")
print("enter 3 for multiplication")
print("enter 4 for division")

choice = int(input("enter your choice:"))


if(choice==1):
    a= int(input("enter your first number: "))
    b= int(input("enter second no: "))
    sum = a + b
    print("add = ",sum)
elif(choice==2):
    a= int(input("enter your first number: "))
    b= int(input("enter second no: "))
    sub = a - b
    print("subract = ",sub)
elif(choice==3):
    a= int(input("enter your first number: "))
    b= int(input("enter second no: "))
    multi = a * b
    print("multiplication",multi)
elif(choice==4):
    a= int(input("enter your first number: "))
    b= int(input("enter second no: "))
    div = a / b
    print("division",div)
else:
    print("you enter wrong choice")