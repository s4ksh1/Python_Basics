# printing common items in two lists

l1 = [1,2,3,4,5,6]
l2 = [9,8,7,6,5,0]
new_list = list()
for x in l1:
    for y in l2:
        if x == y:
            new_list.append(x)
print("Common elements are : ",new_list)


Output:
python common_items.py
Common elements are :  [5, 6]
