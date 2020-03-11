import binascii
import io
from PIL import Image,ImageOps  
from protocol_wrapper_updated import ProtocolWrapper 

pw=ProtocolWrapper()

def input_seq(pw, seq):
	return [pw.input(s) for s in seq]

img_decoded=input_seq(pw,img_coded)
#print(img_decoded)

c=0
lst=''
for b in pw.last_message:	
    c+=1	
    lst+=b
print(c)

image = Image.frombytes("RGB", (640, 480), lst)

b, g, r = image.split()
image = Image.merge("RGB", (r, g, b))

image = ImageOps.flip(image)
image.show()
