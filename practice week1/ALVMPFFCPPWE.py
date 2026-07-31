def ATM_sim():   
    i=int(input("Initial amount: "))
    while True:
        task=input("Deposite(1)/Withdraw(2)/Check Balance(3)/End(4): ").lower()
        if task=="1":
            c=int(input("Enter amount to deposit: "))
            i = i+c
            print("Balance is: ",i)
        elif task=="2":
            d=int(input("Enter amount to withdraw: "))
            i = i-d
            print("Balance is: ",i)
        elif task=="3":
            i=i
            print("Balance is: ",i)
        elif task=="4":
            print("GET LOST")
            break
        else:
            print("Invalid Input")

def login():
    while True:
        task=input("Generate PIN(1), Change PIN(2), Login(3), End(4): ")
        if task=="1":
            pin=input("Enter PIN: ")
            with open("pindb.txt", "w") as file:
                file.write(pin)
            print("PIN Generated.")
        elif task=="2":
            current_pin=input("Enter your current PIN: ")
            with open("pindb.txt", "r") as file:
                old_pin=file.read()
            while True:
                if current_pin==old_pin:
                    new_pin=input("Enter new PIN: ")
                    if new_pin==old_pin:
                        print("Enter anaother PIN")
                    else:
                        with open("pindb.txt", "w") as file:
                            file.write(new_pin)
                        print("PIN Changed")
                        break
                else:
                    print("Enter Correct PIN")
                    break
        elif task=="3":
            check=input("Enter Pin: ")
            with open("pindb.txt", "r") as file:
                old_pin=file.read()
            if check==old_pin:
                ATM_sim()
            else:
                print("Enter Correct PIN")
        elif task=="4":
            print("Program Ending")
            break
        else:
            print("Invalid Input")

def voting_eligibility():
    age=int(input("Enter Age: "))
    if age>=18:
        print("Eligible to Vote.")
    else: 
        print("Not Eligible to vote.")

def multiplication_table():
    t=int(input("Which Table: "))
    for i in range(10):
        print(t,"x",i+1,"=",t*(i+1))

def prime_number():
    num=int(input("Enter Number: "))
    while True:
        if num<=2:
                print("It is a Prime Number.")
                return
        for i in range(2,num):
            if num%i==0:
                print("It is not a Prime Number.")
                break
            elif i==num-1:
                print("It is a prime Number.")
            else:
                continue
        break
        
def fibnacci_series():
    p=int(input("Till which index: "))
    a=0
    b=1 
    for i in range(p):
        print(a,end=",")
        c=a+b
        a=b
        b=c

def factorial():
    fact=int(input("Factorial of: "))
    step=1
    r=0
    for i in range(1,fact+1):
        step,r=step*i,r+step
        
    print(step)

def calculator_using_functions():
    while True:
        task=input("Addition(1), Subtraction(2), Multiplication(3), Division(4), End(5): ")
        if task=="1":
            a=int(input("Enter First Number: "))
            b=int(input("Enter Second Number: "))
            print("Result is: ",a+b)
        elif task=="2":
            a=int(input("Enter First Number: "))
            b=int(input("Enter Second Number: "))
            print("Result is: ",a-b)
        elif task=="3":
            a=int(input("Enter First Number: "))
            b=int(input("Enter Second Number: "))
            print("Result is: ",a*b)
        elif task=="4":
            a=int(input("Enter First Number: "))
            b=int(input("Enter Second Number: "))
            print("Result is: ",a/b)
        elif task=="5":
            print("Program Ending")
            break
        else:
            print("Invalid Input")

def password_checker():
    password=input("Enter Password: ")
    if len(password)<8 and len(password)>16:
        if password.isalnum():
            print("Password is valid.")
        else:
            print("Password is invalid.")
    elif len(password)<8:
        print("Password is too short.")
    elif len(password)>16:
        print("Password is too long.")
    else:
        print("Password is valid.")

def palindrome_checker():
    pall=input("Enter String: ").strip()
    if pall==pall[::-1]:
        print("Palindrome")
    else:
        print("NO")

def word_counter():
    sentence = input("Enter: ").split()
    count = 0
    for i in sentence:
        count += 1
    print(f"Number of words in the given sentence are {count}")    

def email_validator():
    email = input("Enter Email: ")
    if "@" in email:
        if "." in email:
            print(f"You entered a valid: {email}")
        else:
            print("There is no . in your email.")
    else:
        print("There is no @ in your email.")

email_validator()