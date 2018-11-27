import pyautogui
import time
import numpy as np
from PIL import ImageGrab
import fastMeasurement
x = 175
y = 115
mesurment = 35
arrs = np.zeros((16,30),dtype= np.int64)
time.sleep(5)
edge_y = 100
edge_x = 155

mine_1 = pyautogui.locateOnScreen('log.jpg')
print(mine_1)
time.sleep(5)



for i in range(16):
   for j in range(1):
       pyautogui.moveTo(x+ j * mesurment,y + i * mesurment,duration= 1)
       bbox = (edge_x+j * mesurment,edge_y + i * mesurment,edge_x+j * mesurment+mesurment,edge_y + i * mesurment+mesurment)
       img=ImageGrab.grab(bbox)
       str = 'dataset/%d_%d.png' % ((edge_x+j * mesurment),(edge_y + i * mesurment))
       img.save(str)
# for i in range(16):
#     for j in range(1):
#         pyautogui.moveTo(length+ j * mesurment,height + i * mesurment,duration= 1)
#         pyautogui.click()
#         fastMeasurement.moveTotryAgain()
#         pyautogui.click()

