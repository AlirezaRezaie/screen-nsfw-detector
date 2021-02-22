import pyscreenshot as ImageGrab
import cv2
from nudity import Nudity
import os
import pyttsx3
import shutil

depp = [i for i in os.listdir('C:/Users/Lenovo/Desktop/nodyab')]
print(depp)
for i in depp:
    if 'mamad' in i:
        os.remove(i)
    elif 'nude' in i:
        os.remove(i)

def sayy(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

nudity = Nudity()
threshold = 0
while True:
    im = ImageGrab.grab()
    im.save('mamad.png')
    c = nudity.has('mamad.png')
    threshold = threshold + 1
    if c == True:
         os.rename('mamad.png','nude%s.png'%threshold)
         try:
            shutil.move('C:/Users/Lenovo/Desktop/nodyab/nude%s.png'%threshold,'C:/Users/Lenovo/Desktop/nuudes')

         except:
             thresholdnew = threshold+1
             shutil.move('C:/Users/Lenovo/Desktop/nodyab/nude%s.png'%threshold,'C:/Users/Lenovo/Desktop/nuudes/nuude%s.png'%thresholdnew)
         print('shit')
    elif c == False:
        os.remove('mamad.png')
