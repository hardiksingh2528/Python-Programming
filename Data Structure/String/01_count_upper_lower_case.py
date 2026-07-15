"""Write a program to count the number of upper and lower case letters
in a String."""
name = "Hardik Singh"
upper = 0
lower = 0
for letter in name:
    if letter.isupper():
        upper+=1
    elif letter.islower():
        lower+=1
print(upper)
print(lower)