#	Write a program to solve the following equations in java.

#( a )    x=(-b±√(b^2-4ac))/2a

#( b )   F=G (m_1 m_2)/r^2 ,G=6.67×〖10〗^(-11)      (declare ‘G’ as constant) 

"""quadratic equation a*x**2+b*x+c"""
def sol():
    import cmath
    a=float(input('enter a: '))
    b=float(input('enter b: '))
    c=float(input('enter c: '))
#discriminant
    d=(b**2)-(4*a*c)
#solution
    sol1 =(-b-cmath.sqrt(d))/(2*a)
    sol2 =(-b+cmath.sqrt(d))/(2*a)
    return (sol1,sol2)


"""gravitational force"""
def force(m1,m2):
    G=6.67*(10**-11)
    r=6371
    return (G*m1*m2)/r**2
    
    
