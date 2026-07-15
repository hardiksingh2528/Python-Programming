"""Write a program to prepare a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of the keys."""
dic_x={}
for key in range(1,16):
    dic_x[key]=key**2
print(dic_x)