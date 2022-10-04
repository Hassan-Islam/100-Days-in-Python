#Nested if else (you can write the condition within a condition whether 
# the first condition will not true)

height =int(input("what is your height in cm:?"))


if height >=120:
    print ("You can ride the rollercoaster")

    age = int(input("what is your age?"))
    if age <18:
        print ("please pay 5$")
    elif age <=18:
        print ("please pay 7$")
        
    else:
        print ("please pay 12$")

else:
    print ("you cannot the ride.")

