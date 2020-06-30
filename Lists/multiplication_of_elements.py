l = list()
n = int(input("Enter the number of elements you want in list:"))
for i in range(n):
    a = int(input("Enter element to insert in the list:"))
    l.append(a)

print("Your list is:", l)

#Multiplication of elements of list
M=1
for x in l:
    M = M*x

print("Multiplication of elements is :",M)


Output:
python multiplication_of_ele.py
Enter the number of elements you want in list:5
Enter element to insert in the list:5
Enter element to insert in the list:4
Enter element to insert in the list:3
Enter element to insert in the list:2
Enter element to insert in the list:1
Your list is: [5, 4, 3, 2, 1]
Multiplication of elements is : 120
