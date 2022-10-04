#Python pizza order
from re import L
from xmlrpc.server import SimpleXMLRPCDispatcher


print ("Welcome to the python pizza deliveries")
size = input ("what the size of a pizza do you want? S,M,L")
add_pepperoni = input ("Do you want pepperoni?")
extra_cheese = input ("Do you want extra cheese?")


bill =0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size =="S":
        bill += 2
else:
    bill = 3

if extra_cheese =="Y":
        bill += 1
print (f"your final bill is:{bill}")



