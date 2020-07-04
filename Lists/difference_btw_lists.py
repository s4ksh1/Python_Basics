l1 = [1,2,3,4,5,6,7]
l2 = [2,4,6,8,9,10]
print(list(set(l1)-set(l2)))
print(list(set(l2)-set(l1)))


Output:
python difference_btw_lists.py
[1, 3, 5, 7]
[8, 9, 10]
