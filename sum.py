a,b,c = map(int,input("Enter three space seperated numbers: ").split())
if a==b and b==c:
    print(3*(a+b+c))
else:
    print(a+b+c)
    
    
Output:
python sum.py
Enter three space seperated numbers: 3 1 5
9

python sum.py
Enter three space seperated numbers: 2 2 2
18
