"""Question:
Given the participant’s score sheet for your University Sports Day,
you are required to find the runner-up score. You have scores.
Store them in a list and find the score of the runner-up.

Sample Input : [2, 3, 6, 6, 5]
Sample Output : 5

Explanation : Given list is [2, 3, 6, 6, 5].
The maximum score is 6, and the second maximum (runner-up) score is 5.
Hence, we print 5 as the runner-up score."""

N = int(input("Enter the no. of participant : "))
scores=[]
for i in range(1,N):
    scores.append(input("Enter a Score : "))
print(scores)
scores.sort()
print("Runner-up score is : ",scores[-2])
