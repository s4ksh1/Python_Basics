l = list()
for i in range(1,31):
    l.append(i*i)

print("Original list :", l)
print("List of first and last five elements of original list :",l[:5]+l[-5:])


Output:
python first_nd_last_5.py
Original list : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]        
List of first and last five elements of original list : [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]
