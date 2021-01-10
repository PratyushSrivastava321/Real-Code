a=0
x=0
c=0
b=0
z=a*(x**2)+b*x+c
print("according to the equation ax^2+bx+c write the coefficients of the desired quadratic equation u want the zeros of following ")
a=int(input("Coefficient of x2 : " ))
b=int(input("Coefficient of x : "))
c=int(input("constant term is : "))
d=(((b**2)-4*a*c)**1/2)
if d>0:
    x=(-b+d)/2*a
    y=(-b-d)/2*a
    print("the zeros are ",x,"&",y)
elif d==0:
    x=(-b+d)/2*a
    y=x
    print("the zeros are ",x,"&",y)
else:
    print("the zeros are imaginary")


