"""Project: 1
Create a Python program that asks the user how far they want to travel.
If they want to travel less than three miles, tell them to ride Bicycle.
If they want to travel more than three miles, but less than three hundred
miles, tell them to ride Motor-Cycle. If they want to travel three hundred
miles or more, tell them to drive Super-Car.

Sample Output:
How far would you like to travel in miles?
2500
I suggest Super-Car to your destination.
"""
dis=int(input("How far you want to travel (In Miles) ? - "))
if dis<3:
    print("Ride Bicycle")
elif 300>dis>3:
    print("Ride Motor-Cycle")
elif dis>=300:
    print("Drive Supar-Car")


