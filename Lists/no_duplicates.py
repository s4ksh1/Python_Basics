l = list()
n = int(input("Enter the number of elements you want in list:"))
for i in range(n):
    a = int(input("Enter element to insert in the list:"))
    l.append(a)

print("Your list is:", l)

s = set()
for x in l:
    s.add(x)

new_list = list(s)
print("List without duplicates is :",new_list)


Output:
python no_duplicates.py
Enter the number of elements you want in list:6
Enter element to insert in the list:2
Enter element to insert in the list:4
Enter element to insert in the list:4
Enter element to insert in the list:5
Enter element to insert in the list:2
Enter element to insert in the list:4
Your list is: [2, 4, 4, 5, 2, 4]
List without duplicates is : [2, 4, 5]
