def dec_to_q (x,q):
	nx = ""
	Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	while x>0:
		if x%q<10:
			nx+=str(x%q)
		else:
			nx+=str(Alp[(x%q)-10])
		x=x//q
	return str(nx [::-1])
def q_to_dec (x,q):
	nx=0
	k=len(str(x))
	for i in str(x):
		k-=1
		nx+=(q**k)*int(i)
	return nx
print(dec_to_q(13,16))
'''s=input('1 - из десятичной\n2 - в десятичную\n')
if s == '1':
	a,b=map(int,input('введите число, затем основание СС (через пробел)').split())
	print(dec_to_q(a,b))
if s == '2':
	a,b=map(int,input('введите число, затем основание СС (через пробел)').split())
	print(q_to_dec(a,b))'''