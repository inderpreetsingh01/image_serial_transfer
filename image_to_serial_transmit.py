import binascii
import io
from PIL import Image,ImageOps  
from protocol_wrapper_updated import ProtocolWrapper 

image = Image.open('Untitled.png')
print(image.size)

im_resize = image.resize((640, 480))
print(im_resize.size)
#im_resize.show()

buf = io.BytesIO()
im_resize.save(buf, format='bmp')
byte_im = buf.getvalue()

hex_string = binascii.hexlify(byte_im)            #only for debugging
#print(hex_string[:20])                           #only for debugging

pw=ProtocolWrapper()

print(len(byte_im))

#img_coded = pw.wrap((byte_im)[54:])
img_coded = pw.msg_to_packets((byte_im)[54:])


'''
c=0
for i in img_coded:
	print(hex(ord(i)))

	if (c==100):
                break

	c+=1
print(c)
'''

