"""Write a program to iterate over a dictionary using for loop and
print the keys alone, values alone and both keys and values"""

score={1:12,2:19,3:26,4:33}
print("Keys : ",end=" ")
for i in score:
    print(i,end=" ")
print()
print("Values : ",end=" ")
for i in score :
    print(score[i], end=" ")
print()
print("Keys & Values : ")
for i,j in score.items() :
    print(i,":",j)