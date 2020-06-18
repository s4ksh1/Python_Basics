n = int(input("Enter the number of values you want in a list:"))
list=[]
for i in range(n) :
    list.append(int(input()))
    
print("Your list is:", list)
# counting number of four's in the list
count=0
for x in list:
    if x == 4:
        count+=1
print("Number of 4's is:", count)


Output:
python 4s_in_list.py

Enter the number of values you want in a list:8
3
4
5
6
4
1
4
9
Your list is: [3, 4, 5, 6, 4, 1, 4, 9]
Number of 4's is: 3
