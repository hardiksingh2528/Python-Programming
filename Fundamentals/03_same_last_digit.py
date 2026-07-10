'''Given two non-negative values, print true if they have the same
   last digit.

Example:
lastDigit(7, 17) → true
lastDigit(6, 17) → false
lastDigit(3, 113) → true'''

a=int(input('Enter the Value of a : '))
b=int(input('Enter the value of b : '))
if(a%10 == b%10):
    print('true')
else:
    print('false')
