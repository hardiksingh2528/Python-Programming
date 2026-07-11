"""Let's assume you are planning to use your Python skills to build a
PBLApp for Mobile.You decide to host your application on servers running
in the cloud. You pick a hosting provider that charges $0.51 per hour.
You will launch your service using one server and want to know how much
it will cost to operate per day, per week, and per month.

Write a Python program that displays the answers to the following questions:

How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?"""

cost_per_hr=0.51
print("How much does it cost to operate one server per day? - ","$",cost_per_hr*24,)
print("How much does it cost to operate one server per week? - ","$",cost_per_hr*24*7)
print("How much does it cost to operate one server per month? - ","$",cost_per_hr*24*30)
print("How many days can I operate one server with $918? - ",918/(cost_per_hr*24))