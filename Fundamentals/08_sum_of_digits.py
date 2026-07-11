'''Write a program to print the sum of all the digits of a
   given number.

Example:
Input: 1234
Output: 10'''
num = int(input("Enter a Number : "))
sum = 0
while (num!=0) :
    a=num%10
    num=num//10
    sum=sum+a
print(sum)





