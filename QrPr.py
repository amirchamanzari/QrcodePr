import cv2
from pyzbar import pyzbar
path = "testqr.jpeg"
img = cv2.imread(path)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

qrcode = pyzbar.decode(img)

#x,y = qrcode.rect
#cv2.rectangle(img,(x,y),0,0)
#bdata = qrcode.data.decode("utf-8")
#btype = qrcode.type
#text = f"{bdata},{btype}"
#cv2.putText(img,text(x,y-10))
print (qrcode)
