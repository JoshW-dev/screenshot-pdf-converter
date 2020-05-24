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
numPages = 5

time.sleep(3)
#wait 3 seconds before starting

for i in range(numPages):
    #take screenshot 
    myScreenshot = pyautogui.screenshot(region=(left,top,width,height))
    myScreenshot.save(r''+cwd+'\screenshot.png')
    #convert image to pdf and save
    image = Image.open(r''+cwd+'\screenshot.png')
    im = image.convert('RGB')
    im.save(r''+cwd+'\page'+str(i)+'.pdf')
    #press and release space (to go to next page)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    #time buffer
    time.sleep(0.1)

#wait 5 seconds then merge
time.sleep(5)
#create result pdf
pdfs =[] 
for i in range(numPages):
    pdfs.append('page'+str(i)+'.pdf')
merger = PdfFileMerger()
print("pdfs to be merged:")
print(pdfs)
for pdf in pdfs:
    merger.append(open(pdf,'rb'))
with open("result.pdf", "wb") as fout:
    merger.write(fout)

