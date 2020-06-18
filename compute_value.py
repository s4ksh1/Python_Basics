a = int(input("Input an integer : "))       # this program takes an integer(n) as input and compute n+nn+nnn
n1 = int( "%i" % a )                        # example if n=4 then, 4+44+444=492
n2 = int( "%i%i" % (a,a) )
n3 = int( "%i%i%i" % (a,a,a) )
print (n1+n2+n3)


Output:
python compute_value.py

Input an integer : 5
615
