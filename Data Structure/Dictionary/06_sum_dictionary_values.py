"""Write a program to sum all the values in a dictionary, considering
the values will be of int type."""
dict_x = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
sum=0
for key in dict_x :
    sum+=dict_x[key]
print(sum)
