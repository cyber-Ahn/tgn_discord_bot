from decimal import getcontext, Decimal
import time
from commands import debug

def get_pi(debuging,decimal_points):
    getcontext().prec=decimal_points
    accuracy=int(decimal_points/2)
    a=1
    b=1/Decimal(2).sqrt()
    s=1/Decimal(4)
    out = ""
    t0 = time.time()
    for n in range(accuracy):
        A=(a+b)/2
        B=Decimal(a*b).sqrt()
        S=s-2**n*(a-A)**2
        out=A**2/s
        if(debuging):
            debug.write("red", (str(n)+":"+str(out)))
        a=A
        b=B
        s=S
    t1 = time.time()
    return str(out)+"\ntime:"+str(t1 - t0)

if __name__ == "__main__":
    print("This is a library, it can not be started directly.")