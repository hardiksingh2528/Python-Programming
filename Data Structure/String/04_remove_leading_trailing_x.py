"""Given a string, if the first or last character is 'x', return
the string without those 'x' characters, else return the string unchanged.
Example: Input : "xHix"
         Output: "Hi" """
string = input("Enter a string : ")
if string[0]=="x" and string[len(string)-1]=="x":
    print(string[1:len(string)-1])
else:print(string)

