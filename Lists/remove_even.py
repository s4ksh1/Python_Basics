l = list()
n = int(input("Enter number of elements you want in list :"))
for i in range(n):
    a = int(input())
    l.append(a)

print("Original list :",l)
for x in l:
    if x%2==0:
        l.remove(x)

print("List after removing even numbers :",l)


Output:
python remove_even.py
Enter number of elements you want in list :5
1
2
3
4
5
Original list : [1, 2, 3, 4, 5]
List after removing even numbers : [1, 3, 5]
