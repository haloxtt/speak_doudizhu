#coding=utf-8
import pyautogui
import cv2
import numpy as np
import time
import ImageMatch

targetPath = "全部.jpg"
img = pyautogui.screenshot() # x,y,w,h
rgb_im = img.convert('RGB')
rgb_im.save(targetPath)

# time.sleep(3)
# templatePath="/Users/xietaotao/Documents/编码奇才/image/方尖.jpg"
# targetPath="/Users/xietaotao/Documents/编码奇才/image/全部.jpg" 
# result=ImageMatch.imageMatch(targetPath,templatePath)
# pyautogui.click(result[0],result[1])
