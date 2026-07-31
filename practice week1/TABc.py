from datetime import date

def temp_convertor():
    temp = float(input("Enter Temperature: "))
    unit = input("Temperature type celsius or fahrenheit: ").lower()
    if unit == "celsius" or unit == "c":
        converted_temp = temp * (9/5) + 32 
    elif unit == "fahrenheit" or unit == "f": 
        converted_temp = ((temp -32)*5)/9
    else:
        return "Invalid unit. Please enter 'celsius' or 'fahrenheit'."
    #result = converted_temp + "Fahrenheit" if unit == "celsius"  else "Celsius"
    return str(converted_temp) + " in Fahrenheit." if unit == "celsius" or unit == "c" else str(converted_temp) + " in Celsius."

def age_calc():
    birth_year = int(input("Enter Birth Year: "))
    cyear = date.today().year
    if birth_year > cyear:
        return "Birth year cannot be in the future."
    age = cyear - birth_year
    return f"Your current age is {age}."

def bmi_calc():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in KG: "))
    bmi = weight/(height**2)
    return f"Your BMI is {bmi:.2f}."

while True:

    selection = int(input("Select what you want to do 1 for Temperature convertor, 2 for Age calc, 3 for BMI calc, 4 for End: "))
    if selection==1:
        print(temp_convertor())
    elif selection==2:
        print(age_calc())
    elif selection==3:
        print(bmi_calc())
    elif selection==4:
        print("Program ending...")
        break
    else:
        print("Do proper selection")