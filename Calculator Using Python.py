def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Mul(a,b):
    return a*b

def Div(a,b):
    return a/b

print("Select the operation for performing")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:

    choose = input("Choose the value(1/2/3/4):")
    if choose in ('1','2','3','4'):
          num1= float(input("Enter the first Number:"))
          num2= float(input("Enter the second Number:"))

          if choose=='1':
            print(num1,"+",num2,"=",Add(num1,num2))

          elif choose=='2':
            print(num1,"-",num2,"=",Sub(num1,num2))

          elif choose=='3':
            print(num1,"*",num2,"=",Mul(num1,num2))

          elif choose=='4':
            print(num1,"/",num2,"=",Div(num1,num2))

          NextCal=input("Want to perform next calculation?(yes/no):")
          if NextCal=="no":
           break

    else:
            print("Invalid Operation")

   
    
