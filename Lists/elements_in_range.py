# finding number of elements in range (30,60)

l = [67,54,87,56,99,34,2,3,66,5,30,39,45,51]
count=0
for x in l:
    if x>=30 and x<60:
        count+=1

print("Number of elements in specified range are :",count)


Output:
python elements_in_range.py
Number of elements in specified range are : 7
