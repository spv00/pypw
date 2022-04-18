X=range
W=float
M='-'
L=''
K=str
J=int
E='\r'
A=print
import os,sys,hashlib as B,random as D,string as C,subprocess as N,re
O=sys.argv
F=26
try:F=J(O[1])
except Exception:pass
Y=sys.platform
Z=L
def G():C=K(N.check_output(['/usr/bin/xdotool','getmouselocation']).decode().strip());A(E,end=E);B=re.match('x:([0-9]+) y:([0-9]+) .*',C);return B.group(1),B.group(2)
def P(iterations):
	B=G();C=0
	while C<iterations:
		A=G()
		if A!=B:B=A;C+=1;yield(A[0],A[1])
def H(i,text,maxval):B=J(100*W(i)/W(maxval));C=J(B*os.get_terminal_size().columns/100-len(text));A(text+M*C,end=E)
def Q(iterations):
	F='Please move your mouse';B=iterations;C=0;A(F,end=E)
	for D in P(B):C+=1;H(C,F,B);yield D
def I(hash,passes,index):
	E=passes;hash=hash.strip().encode();F={'md5':B.md5,'sha256':B.sha256,'sha512':B.sha512};C=0
	for C in X(E):I,G=D.choice(list(F.items()));hash=G(hash).hexdigest().strip().encode();H(C,f"Hashing pass {C}: ",E);C+=1
	hash=B.sha512(hash).hexdigest().strip().encode();A();return K(hash)
def R(seed,length):
	A=seed;B=L
	for E in X(length):A=I(A,100000,E+1);D.seed(A);B+=D.choice(C.ascii_letters+C.punctuation+C.digits)
	return B
S=[A for A in Q(1000)]
T=L.join([K(A[0]+A[1])[-1:]for A in S])
A()
U=I(T,1000000,0)
V=R(U,F)
A(M*os.get_terminal_size().columns)
A(V)
A(M*os.get_terminal_size().columns)