l = list()
n = int(input("Enter the number of elements you want in list:"))
for i in range(n):
    a = int(input("Enter element to insert in the list:"))
    l.append(a)

print("Your list is:", l)

#sum of elements of list
sum=0
for x in l:
    sum = sum+x

print("Sum of elements is :",sum)


Output:
python sum_of_elements.py
Enter the number of elements you want in list:5
Enter element to insert in the list:5
Enter element to insert in the list:4
Enter element to insert in the list:3
Enter element to insert in the list:2
Enter element to insert in the list:1
Your list is: [5, 4, 3, 2, 1]
Sum of elements is : 15
