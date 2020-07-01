l1 = [1,2,3,4,5]
l2 = [9,8,7,6,5,4]
a = "false"
for x in l1:
    for y in l2:
        if x == y:
            a = "True"
            break
print(a)

Output:
python common_ele.py
True




l1 = [1,2,3,4,5]
l2 = [10,9,8,7,6]
a = "false"
for x in l1:
    for y in l2:
        if x == y:
            a = "True"
            break
print(a)

Output:
python common_ele.py
false
