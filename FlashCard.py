class FlashCard(object):
    def __init__(self):
        self.__front_label = ''
        self.__back_label = ''
        self.__image_path = ''

    def setText(self, front, back):
        '''Set flashcard labels
        input:  front   : str
                back    : str
        output: None
        '''
        self.__front_label = front
        self.__back_label = back

    def getLabels(self):
        '''Returns front and back label
        input:  None
        output: (front_label, back_label) : (str, str)
        '''
        return (self.__front_label, self.__back_label)

    def setImage(self, image):
        '''Set flashcard image filepath
        input:  Path to file locally : str
        output: None
        '''
        self.__image_path = image

    def getImage(self):
        '''Returns flashcard's image filepath
        input:  None
        outout: image_path : str
        '''
        return self.__image_path

#This is test code, it does not run when this file is imported as a module by other scripts
if __name__ == '__main__':
    x = FlashCard()
    x.setText('this is front', 'this is back')
    f,b = x.getLabels()
    x.setImage('C:/users/gavin/pic.jpg')
    z = x.getImage()
    print(z)
    print(f)
    print(b)