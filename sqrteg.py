class SqrtegError(Exception): pass  
class TypeError(SqrtegError):pass
class OutOfRangeError(SqrtegError): pass

def sqIt(n):
	if type(n)==int or type(n)==float:
		return n**2		
	else:	
		raise TypeError,"Invalid"


def sqrtIt(n):
	if n<0:
		raise OutOfRangeError,"No negatives please"
	if type(n)==int or type(n)==float :
		return n**.5
	else:	
		raise TypeError,"Invalid"

