from miller import *
import sys
import hashlib
import math

#function to compute inverse
def computeInverse (in1,in2):
    aL = [in1]
    bL = [in2]
    tL = [0]
    t = 1
    sL = [1]
    s = 0
    q = math.floor((aL[0]/bL[0]))
    r = (aL[0] - (q*bL[0]))

    while r > 0 :
        temp = (tL[0] - (q*bL[0]))
        tL[0] = t
        t = temp
        temp = (sL[0] - (q*s))
        sL[0] = s
        s = temp
        aL[0] = bL[0]
        bL[0] = r
        q = math.floor(aL[0]/bL[0])
        r = (aL[0] - (q*bL[0]))

    r = bL[0]

    inverse = s % in2
    return inverse


def squareAndMultiply(x,c,n):
	z=1
	#getting value of l by converting c into binary representation and getting its length
	c="{0:b}".format(c)[::-1] #reversing the binary string
	
	l=len(c)
	for i in range(l-1,-1,-1):
		z=pow(z,2)
		z=z%n
		if(c[i] == '1'):
			z=(z*x)%n
	return z	

def shaHash(fileName):
	BLOCKSIZE = 65536
	hasher = hashlib.sha1()
	with open(fileName, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
	#print(hasher.hexdigest())
	hex = "0x"+hasher.hexdigest()
	#print(int(hex,0))
	return int(hex,0) #returns int value of hash

def sign():
	if(len(sys.argv) < 2):
		print("Format: python sign.py filename")
	elif(len(sys.argv) == 2):	
		print("Signing the file...")
		fileName = sys.argv[1]
		
		file1 = open("key.txt","r")
		file2 = open("secretkey.txt","r")
		p=int(file1.readline().rstrip())
		q=int(file1.readline().rstrip())
		g=int(file1.readline().rstrip())
		h=int(file1.readline().rstrip())
		a=int(file2.readline().rstrip())
		
		loop = True
		while loop:
			r = random.randint(1,q-1)
			c1 = squareAndMultiply(g,r,p)
			c1 = c1%q
			c2 = shaHash(fileName) + (a*c1)
			Rinverse = computeInverse(r,q)
			c2 = (c2*Rinverse)%q
			
			if(c1 != 0 and c2 != 0):
				loop = False
		
		#print(shaHash(fileName))	
		#print(c1)	
		#print(c2)	
		file = open("signature.txt","w")
		file.write(str(c1))
		file.write("\n")
		file.write(str(c2))
		print("cipher stored at signature.txt")
sign()