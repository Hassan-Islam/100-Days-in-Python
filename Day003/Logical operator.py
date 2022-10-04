#Logical operator
print ("Welcome to the rollercoaster")
height = int(input ("what is your height in cm?"))
bill = 0

if height <=120:
    print ("you can ride the rollercoaster")
    age = int(input ("what is your age?"))
    if age <18:
        bill = 5
        print ("Child ticket is 5$")
    elif age <= 18:
        bill = 7
        print ("youth ticket are 7$")

    elif age >= 45 and age <= 55:

        print ("Everything will be perfect.")
        bill= 12
        print ("Adult ticket are 12$")


    want_bill = input ("Do you want a photo taken ?Y,N.")
    if want_bill == "Y":
        bill += 3
        print (f"your final bill {bill}")

else:
    print ("you are too small")