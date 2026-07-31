def grade_calc():
    glist=[]
    for i in range(5):
        grades=int(input("Enter marks of sub: "))
        glist.append(grades)
    sum = 0
    for i in glist:
        sum = sum + i 
    grade = (sum/500)*100
    if grade >= 90:
        result=("Noice Grade",grade)
    elif grade < 90 and grade >=40:
        result=("Average Grade",grade)
    else:
        result=("Go Die LOW LIFE",grade)
    return result

# r=grade_calc()
# print(r)

def discount_calc():
    price= float(input("Enter Price: "))
    discount= float(input("Enter Discount: "))
    sub_a= price*discount/100
    discounted_amount= price - sub_a
    return discounted_amount

# print(discount_calc())

def leap_year_checker():
    year=int(input("Enter Year: "))
    if year%4==0 and year%100!=0:
        result=("It is a leap year.")
    elif year%4==0 and year%100==0:
        if year%400==0:
            result=("It is a leap year.")
        else:
            result=("It is not a leap year.")
    else:
        result=("It is not a leap year.")
    return result

# print(leap_year_checker())
print("========Menu======== \n 1 for Grade calculator \n 2 for Discount calculator \n 3 for Leap year checker \n 4 to END Program")

while True:

    selection = int(input("Select what you want to do: "))
    if selection==1:
        print(grade_calc())
    elif selection==2:
        print(discount_calc())
    elif selection==3:
        print(leap_year_checker())
    elif selection==4:
        print("Program ending...")
        break
    else:
        print("Do proper selection")