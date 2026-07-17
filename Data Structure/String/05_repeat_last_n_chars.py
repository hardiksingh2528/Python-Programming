"""Given a string and an integer n, return a string made of n
repetitions of the last n characters of the string. You may assume
that n is between 0 and the length of the string inclusive.
Example:
Input : "Wipro", n = 3
Output: "propropro" """
string = input("Enter a String : ")
integer = int(input("Enter an Integer : "))
output = ""
for i in range(integer):
    a = string[-integer:]
    output+=a
print(output)

