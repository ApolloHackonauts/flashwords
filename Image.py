# import the necessary packages
import cv2

class Image(object):

    def __init__(self, imageLocation):
        # saves image location in this object
        self.image = cv2.imread(imageLocation, 0)
    
    def cropAt(self, x, y, w, h, saveLocation):
        # saves a croped version of the whole image
        crop_img = self.image[y:y+h, x:x+w]
        cv2.imwrite(saveLocation, crop_img)
        

