l = list()
n = int(input("Enter the number of elements you want in list:"))
for i in range(n):
    a = int(input("Enter element to insert in the list:"))
    l.append(a)

print("Your list is:", l)

l.sort()

print("Sorted list is :",l)
print("Smallest element of list is :",l[0])


Output:
python smallest_element.py
Enter the number of elements you want in list:5
Enter element to insert in the list:2
Enter element to insert in the list:8
Enter element to insert in the list:3
Enter element to insert in the list:9
Enter element to insert in the list:6
Your list is: [2, 8, 3, 9, 6]
Sorted list is : [2, 3, 6, 8, 9]
Smallest element of list is : 2
