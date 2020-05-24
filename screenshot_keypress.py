import os
import time
from PIL import Image
import pyautogui
from pynput.keyboard import Key, Controller
from PyPDF2 import PdfFileMerger

keyboard = Controller()
cwd = os.getcwd()
merger = PdfFileMerger
pdfs=[]

#screenshot location and size
left = 619
top = 44
width = 669
height = 1005

#number of screenshots to take
numPages = 315

time.sleep(3)
#wait 3 seconds before starting

for i in range(numPages):
    #take screenshot 
    myScreenshot = pyautogui.screenshot(region=(left,top,width,height))
    myScreenshot.save(r''+cwd+'\screenshot.png')
    #convert image to pdf
    image = Image.open(r''+cwd+'\screenshot.png')
    im = image.convert('RGB')
    im.save(r''+cwd+'\page'+str(i)+'.pdf')
    #Merge new pdf to master
    pdfs.append('page'+str(i)+'.pdf')
    #press and release space (to go to next page)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    #time buffer
    time.sleep(0.1)

#create result pdf

for pdf in pdfs:
    merger.append(open(pdf,'rb'))
with open ("result.pdf", "wb") as fout:
    merger.write(fout)
