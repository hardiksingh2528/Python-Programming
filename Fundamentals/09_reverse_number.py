"""Write a program to reverse a given number and print
EX 1
input = 1234
output = 4321

EX 2
input = 1004
output = 4001"""
num = int(input("Enter a Number : "))
reverse=""
while(num!=0):
    a=str(num%10)
    num=num//10
    reverse=reverse+a
print(reverse)
