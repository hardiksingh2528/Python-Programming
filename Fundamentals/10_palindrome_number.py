"""Write a program to find if the given number is palindrome or not
EX 1
I/P = 1100011
O/P = 1100011 is a palindrome

EX 2
I/P = 1234
O/P = 1234 is not a palindrome """
num= int (input("Enter a number : "))
original=num
reverse=""
while (num!=0):
    a=str(num%10)
    num=num//10
    reverse=reverse+a
if int(reverse)==original :

    print(original,"is a palindrome")
else:
    print(original,"is not a palindrome")


