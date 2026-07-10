'''Write a program to check if a given number is Prime or Not.'''
num=int(input('Enter a number : '))
if(num<=1):
    print(num,"is not Prime.")
else:
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not Prime.")
            break
    else:
        print(num,"is Prime.")