# import the necessary packages
import cv2

class Image(object):

    def __init__(self, imageLocation):
        # saves image location in this object
        self.image = cv2.imread(imageLocation, 0)
    
    def cropAt(self, x, y, x2, y2, saveLocation='default.jpg'):
        # saves a croped version of the whole image
        crop_img = self.image[y:y2, x:x2]
        cv2.imwrite(saveLocation, crop_img)

if __name__ == '__main__':
    pass
    #test code goes here