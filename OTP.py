import PRG #we need to import the pseudo random number generator
msg=input("enter message: ") #Here is your msg that has to be encrypted 
key=int(input("enter key: ")) # key
code=0
for i in msg:
    code=code*1000+ord(i)
##CountBin counts the number of binary digits the msg conv into binary contains
def CountBin(num):
    count=0;n=0
    while(num>0):
        n=n*10+num%2
        count+=1
        num=num//2
    return count
count=CountBin(code)
prgkey=PRG.CreateKey(key,count)
crypt=code^prgkey #XOR operation
# converting into char
def convchar(val):
    str=''
    while(val>0):
        rem=val%1000
        str=str+chr(rem)
        val=val//1000
    string=''
    for i in range (len(str)):
        string=string+str[len(str)-(i+1)]
    return string
crypttext=convchar(crypt)
print(crypttext)
code=0
for i in crypttext:
    code=code*1000+ord(i)
#Decrypting the cipher text
decrypt=code^prgkey
decipher=convchar(decrypt)
print(decipher)
