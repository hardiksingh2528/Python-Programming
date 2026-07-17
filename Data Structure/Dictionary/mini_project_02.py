"""Project Description
You have a record of n students. Each record contains the student's name
and their percent marks in Math, Physics, and Chemistry. The marks can
be floating values. You are required to save the record in a dictionary
data type.
The student's name is the key. The marks stored in a list are the value.
The user enters a student's name. Output the average percentage marks
obtained by that student.

Formula
Average = (sum of marks) / (number of subjects)
Sample Input
{
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}
Sample Output
Enter a name: Malika
Average percentage mark: 56

Explanation
Marks for Malika are:
[52, 56, 60]
Average:
(52 + 56 + 60) / 3 = 56
Hence, the average percentage mark is 56."""

students={
    "krishna": [67, 68, 69],
    "arjun": [70, 98, 63],
    "malika": [52, 56, 60]
}
print("Students\tmarks")
for name , marks in students.items():
    print(name,"-",marks)

name = input("Enter the name of student from the list : ")
marks = students[name]
average = sum(marks)/len(marks)
print("Average percentage marks : ",average)
