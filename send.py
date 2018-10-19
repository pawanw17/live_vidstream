import cv2
import socket
import time
import math
#ADDRESS='192.168.1.197'
ADDRESS='127.0.0.1'
#ADDRESS='192.168.1.231'
port=12000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("connected")
cap=cv2.VideoCapture(0)
j=1
time.sleep(5)
while (1):
	ret,frame =cap.read()
	data = cv2.imencode('.jpg', frame)[1].tostring()
	frn="fr_"+str(j)+".jpg"
	print(frn)
	i=1
	k=len(data)/65000
	m=len(data)%65000
	k=math.ceil(k)
	p=0
	q=65000
	sts1=bytearray()
	while(i<=k):
		sts=data[p:q]


		s.sendto(sts,(ADDRESS,port))
		print("sending")
		if(i==k-1):
		 	p+=65000
		 	q+=m
		 	sts=data[p:q]
		 	s.sendto(sts,(ADDRESS,port))
		 	break
		else:
		 	p+=65000
		 	q+=65000
		i+=1
	s.sendto(b"masala",(ADDRESS,port))
	print("masala")
	print("masala")
	j+=1
cap.release()
cv2.destroyAllWindows()
s.close()