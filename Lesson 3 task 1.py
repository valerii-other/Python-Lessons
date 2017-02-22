import cmath

a,b,c, = input("Please input a,b,c coeffs:")

root1 = 0
root2 = 0

D = b**2 - 4*a*c

if D == 0:
    root1=root2=-b/(2*a)
elif (D > 0):
    root1 = ((-b - cmath.sqrt(D))/(2*a)).real
    root2 = ((-b + cmath.sqrt(D))/(2*a)).real
elif (D < 0):
    root1 = (-b - cmath.sqrt(D))/(2*a)
    root2 = (-b + cmath.sqrt(D))/(2*a)

if complex(root1):
    print ('Det is {:.2f}. Root1 is {:.2f}. Root2 is {:.2f}.'.format(D, root1, root2))
else:
    print ('Det is {:.2f}. Root1 is {:.2f}. Root2 is {:.2f}'.format(D, root1, root2))
