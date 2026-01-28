import cv2 as cv
import numpy as np
import urllib.request

def read_img_url(url):
   req = urllib.request.urlopen(url)
   img_rw = np.asarray(bytearray(req.read()), dtype=np.uint8)
   img =cv.indecode(img_rw, 0)

   return req

if "_name__" == "__main__":
    url= "https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
    print(read_img_url(url))
    cv.imshow("img",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    
