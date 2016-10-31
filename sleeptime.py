a,b=[int(x) for x in raw_input().split(":")]
c,d=[int(x) for x in raw_input().split(":")]

def getA(e):
    global a
    if e>=c:
        a=e-c
    else:
        a=24+e-c
if b>=d:
    b = b-d
    getA(a)
else:
    b=60+b-d
    a=a-1
    getA(a)
    
if a<10 and b<10:
    print "0"+str(a)+":"+"0"+str(b)
if a>10 and b<10:
    print str(a)+":"+"0"+str(b)
if a>10 and b>10:
    print str(a)+":"+str(b)
if a<10 and b>10:
    print "0"+str(a)+":"+str(b)