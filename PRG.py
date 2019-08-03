def ConvertBin(num):
    n=0;count=0;x=num
    binarylist=[]
    while(num>0):
        #n=n*10+num%2
        binarylist.append(num%2)
        #count+=1
        num=num//2
    binarylist.reverse()
    return binarylist
x=ConvertBin(13)
def CreateKey(key,count):
    prg=[0 for i in range (count)]
    keybin=ConvertBin(key)
    keycount=len(keybin)
    for i in range(keycount):
        prg[i]=keybin[i]
    n=keycount
    for i in range (keycount+1,count):
        #print(prg)
        #print((3*(i+30))%(n-2),(7**i)%(n-2),(n-2),prg[((3*(i+30))%(n-2))]*prg[((7*(i+34))%(n-2))],sep="    ")
        prg[i]=prg[((3*(i+30))%(n-2))]*prg[((7*(i+34))%(n-2))]
        n=n+1
    for i in range (count-2):
        if prg[i]==0 and prg[i+1]==0 and prg[i+2]==0:
            prg[i+1]=1
        if prg[i]==1 and prg[i+1]==1 and prg[i+2]==1:
            prg[i+1]=0
    Reqkey=ConvNum(prg)
    return Reqkey
    
def ConvNum(n):
    num=0
    n.reverse()
    for i in range (len(n)):
        num=num+n[i]*2**i
    return num
