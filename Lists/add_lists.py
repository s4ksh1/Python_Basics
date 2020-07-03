# using '+' operator

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
new_list = l1+l2
print(new_list)


Output:
python add_lists.py
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']


# using append()

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

for x in l2:
    l1.append(x)

print(l1)


Output:
python add_lists.py
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']


# using extend()

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
l1.extend(l2)

print(l1)


Output:
python add_lists.py
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
