'''x are the places of the car and t is the time between them'''

def Velocity(x1,x2,x3,t):
    v2 = (x3-x1)/(2*t)
    return (v2)

def Acceleration(x1,x2,x3,t):
    v1 = (x2-x1)/t
    v3 = (x3-x2)/t
    a2 = (v3-v1)/t
    return (a2)

def ExpectedPoint(x1,x2,x3,t):
    v2 = Velocity(x1,x2,x3,t)
    a2 = Acceleration(x1,x2,x3,t)
    x4 = x2+2*t*v2+2*t*t*a2
    return (x4)





