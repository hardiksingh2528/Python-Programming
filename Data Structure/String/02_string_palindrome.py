"""Write a program that will check whether a given String is
Palindrome or not."""

string = input("Enter a String : ")
string.upper()
reverse = string[ ::-1]
if string==reverse:
    print(string,"is a Palindrome")
else:
    print(string,"is not a Palindrome")



