def add(a,b):
    answer=a+b
    print("")
    print('Addition value is : ',answer ,"\n")
    print("")
def sub(a,b):
    answer=a-b
    print('Subtraction value is : ',answer)
    print("")
def mul(a,b):
    answer=a*b
    print('Multiplication value is : ',answer)
    print("")
def div(a,b):
    answer=a/b
    print('Division value is : ',answer)
    print("")




print('1.Addition')
print('2.Subtration')
print('3.Multiplication')
print('4.Division')
print("5.Exit")
print("")



while True:
    choice=input("Enter your choice : ")
    print("")
    if choice=='1':
        a=int(input("Enter First Number : "))
        b=int(input("Enter Second Number : "))
        add(a,b)
        
    elif choice=='2':
        a=int(input("Enter First Number : "))
        b=int(input("Enter Second Number : "))
        sub(a,b)
        
    elif choice=='3':
        a=int(input("Enter First Number : "))
        b=int(input("Enter Second Number : "))
        mul(a,b)
        
    elif choice=='4':
        a=int(input("Enter First Number : "))
        b=int(input("Enter Second Number : "))
        div(a,b)
        
    elif choice=='5':
        print("Program ended")
        quit()

