"""Write a program to remove a given item from the set."""
set_1 = {"admin",500,"user",500,800}
print(set_1)
item = input("Enter a item to remove : ")
if item in set_1:
    set_1.remove(item)
    print(set_1)
else:
    print("item is not present in set ")
