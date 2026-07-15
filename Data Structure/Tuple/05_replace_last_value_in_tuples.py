"""Write a program to replace last value of tuples in a list to 100.
Sample List : [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output : [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"""

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(sample_list)) :
    li=list(sample_list[i])
    li[2]=100
    tup=tuple(li)
    sample_list[i]=tup
print(sample_list)

