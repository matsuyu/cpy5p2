#Finding the two highest scores
n=int(input("Enter the number of students:"))
arr = [[0 for i in range(100)] for i in range(100)]
max=0
for i in range(n):
    arr[1][i]=str(input("Student's name:"))
    arr[2][i]=int(input("Student's score:"))
    if arr[2][i]>arr[2][max]:
        max=i
print("The highest score:",arr[1][max],arr[2][max])
arr[2][max]=int(0)
for i in range (n):
    if arr[2][i]>arr[2][max]:
        max=i
print("The second highest score:",arr[1][max],arr[2][max])
