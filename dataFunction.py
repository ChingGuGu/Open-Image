import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os, re, copy

#parameter
imageFolder = './database'
file = pd.read_excel('./answer.xlsx')
fixWidth = 600

class App():
    def __init__(self,fixHeight):
        self.fixHeight = fixHeight

    def execute(self, imgId, isQuery=1):
        self.imgId = imgId

        # get image list from image folder
        imageList = list(filter(re.compile('.+.jpg').match, os.listdir(imageFolder)))
        # get question list from excel
        questionList = list(file['answer'])

        if self.imgId >= len(questionList):
            return []
        
        if pd.isnull(questionList[self.imgId]):
            return ['isSpace']
        
        self.imgName = list(filter(re.compile('.+_%s.jpg'%questionList[self.imgId]).match, imageList))[0]

        # if self.imgId >= len(imageList):
        #     return []
        # self.imgName = imageList[self.imgId]
        img, imgH, imgW = self.openImg(self.imgName)

        #[imgAnswer,selection1,selection2,selection3,selection4]
        answerList = self.getAnswer()

        dataList = [img, imgH, imgW, answerList]
        return dataList
    
    # def grouping(self):
    #     imgGroup = self.imgName.split('_')[0]
    #     print(imgGroup)

    def getAnswer(self): # anwser and selection
            imgAnswer = self.imgName.split('_')[1].split('.')[0]

            selection1 = list(file[file.answer==imgAnswer]['selection1'])[0]
            selection2 = list(file[file.answer==imgAnswer]['selection2'])[0]
            selection3 = list(file[file.answer==imgAnswer]['selection3'])[0]
            selection4 = list(file[file.answer==imgAnswer]['selection4'])[0]

            answerList = [imgAnswer,selection1,selection2,selection3,selection4]

            return answerList
    
    def openImg(self, imgName):
        fixHeight = self.fixHeight
        # print(self.imgId, imgName)
        img = Image.open(os.path.join(imageFolder, imgName))
        imgShape = np.shape(img)

        # Resize Picture
        imgWidth = int(imgShape[1]*fixHeight/imgShape[0])
        imgR = img.resize((imgWidth,fixHeight)) #image after resize
        # imgR.save(os.path.join(imageFolder, 'resize','%dx%d_'%(imgWidth,fixHeight)+imgName))

        if imgWidth < fixWidth:
            xBorder = int((fixWidth-imgWidth)/2)

            imgNew = Image.new('RGB',(600,400),'white')
            imgNew.paste(imgR,(xBorder,0))
        
        elif imgWidth >= fixWidth:
            xCrop = int((imgWidth-fixWidth)/2)
            imgNew = imgR.crop((xCrop,0,imgWidth-xCrop,fixHeight))
        
        else:
            imgNew = imgR
        
        # plt.imshow(imgNew)
        # plt.show()
        # imgNew.save(os.path.join(imageFolder, 'resize','%dx%d_'%(np.shape(imgNew)[0],np.shape(imgNew)[1])+imgName))

        # print(np.shape(imgNew)[0],np.shape(imgNew)[1])
        # print(fixHeight, int(imgShape[1]*fixHeight/imgShape[0]))
        # print(np.shape(imgR)[1], np.shape(imgR)[0])
        # return imgR, fixHeight, int(imgShape[1]*fixHeight/imgShape[0])
        return imgNew, np.shape(imgNew)[0], np.shape(imgNew)[1]

if __name__ == '__main__':
    app = App(400)
    app.execute(1)

