import tkinter as tk
import numpy as np
import pandas as pd
from dataFunction import App
from PIL import ImageTk, Image
# from PIL import Image, ImageDraw, ImageFont, 
# import matplotlib.pyplot as plt
# import os, re, copy

#parameter
xCD = 1000
yCD = 600
xShift = 10
yShift = 10
fixHeight = 400 #picture height
(xSel, ySel, space) = (800,10,50) #selection position
(xAns, yAns, space) = (650,10,50) #answer position


class GUI():
    def __init__(self):
        self.imgId = 0
    
    def nextImg(self):
        self.cleanSelection()
        self.cleanAns()

        self.imgId = self.imgId+1
        # query data
        dataList = app.execute(self.imgId)

        if len(dataList) <= 0:
            self.label_img.config(image='')
            return
        
        if 'isSpace' in dataList:
            self.nextImg()
            return

        img = dataList[0]
        imgH = dataList[1]
        imgW = dataList[2]
        self.answerList = dataList[3]

        print(imgW,imgH)

        tkImg = ImageTk.PhotoImage(img)
        self.label_img.imgtk=tkImg
        self.label_img.config(image=tkImg,width=imgW, height=imgH)

    def cleanSelection(self):
        try:
            self.label_selection1.config(text='')
            self.label_selection2.config(text='')
            self.label_selection3.config(text='')
            self.label_selection4.config(text='')
        except:
            return
        
    def cleanAns(self):
        try:
            self.label_answer.config(text='')
        except:
            return
    
    def showAns(self):
        answer = self.answerList[0]
        font = ('微軟正黑體',15,'bold')
        self.label_answer = tk.Label(text='%s'%answer,font=font)
        self.label_answer.place(x=xAns,y=yAns+space)
    
    def showSelection(self):
        answerList = self.answerList
        selection1 = answerList[1]
        selection2 = answerList[2]
        selection3 = answerList[3]
        selection4 = answerList[4]

        font = ('微軟正黑體',15,'bold')
        self.label_selection1 = tk.Label(text='(A) %s'%selection1,font=font)
        self.label_selection1.place(x=xSel,y=ySel+space)
        self.label_selection2 = tk.Label(text='(B) %s'%selection2,font=font)
        self.label_selection2.place(x=xSel,y=ySel+space*2)
        self.label_selection3 = tk.Label(text='(C) %s'%selection3,font=font)
        self.label_selection3.place(x=xSel,y=ySel+space*3)
        self.label_selection4 = tk.Label(text='(D) %s'%selection4,font=font)
        self.label_selection4.place(x=xSel,y=ySel+space*4)

    def execute(self):
        window = tk.Tk()
        window.title("Picture")
        window.geometry("%dx%d+%d+%d"%(xCD,yCD,xShift,yShift))
        window.resizable(False,False)

        # query data
        dataList = app.execute(self.imgId)        

        if len(dataList) <= 0:
            self.label_img.config(image='')
            return
        
        if 'isSpace' in dataList:
            self.nextImg()
            return


        img = dataList[0]
        imgH = dataList[1]
        imgW = dataList[2]
        self.answerList = dataList[3]

        # input image
        tkImg = ImageTk.PhotoImage(img)
        self.label_img = tk.Label(window,width=imgW, height=imgH,image=tkImg)
        self.label_img.place(x=10,y=10)

        # create button: NEXT PIC
        font = ('微軟正黑體',15,'bold')
        button_next = tk.Button(window,text='下一張',font=font,command=self.nextImg)
        button_next.place(x=int(600/2),y=450)

        # create button: SHOW ANSWER
        button_answer = tk.Button(window,text='看答案',font=font,command=self.showAns)
        button_answer.place(x=xAns,y=yAns)

        # create button: SHOW SELECTION
        button_selection = tk.Button(window,text='看選項',font=font,command=self.showSelection)
        button_selection.place(x=xSel,y=ySel)
        


        window.mainloop()
    
    
if __name__ == '__main__':
    app = App(fixHeight)
    gui = GUI()
    gui.execute()