"""Given a string, return a new string made of n copies of the first 2
characters of the original string, where n is the length of the string.
The string length will be >= 2.
Example: Input : "Wipro"
         Output: "WiWiWiWiWi" """
string = input("Enter a String : ")
output = ""
for i in range(len(string)):
    a = string[:2]
    output+=a
print(output)
