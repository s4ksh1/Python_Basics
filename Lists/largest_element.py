l = list()
n = int(input("Enter the number of elements you want in list:"))
for i in range(n):
    a = int(input("Enter element to insert in the list:"))
    l.append(a)

print("Your list is:", l)

l.sort()

print("Sorted list is :",l)
print("Largest element of list is :",l[-1])


Output:
python largest_element.py
Enter the number of elements you want in list:5
Enter element to insert in the list:2
Enter element to insert in the list:7
Enter element to insert in the list:1
Enter element to insert in the list:9
Enter element to insert in the list:4
Your list is: [2, 7, 1, 9, 4]
Sorted list is : [1, 2, 4, 7, 9]
Largest element of list is : 9
