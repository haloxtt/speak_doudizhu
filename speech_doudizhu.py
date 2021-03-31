#coding=utf-8
import ImageMatch
import VoiceRecording
import TencentRecognition
import pyautogui
import cv2
import numpy as np
import time

def matchPoker(poker,count):
    try:
        if count == '一':
            count = 1
        if count == '两':
            count = 2
        if count == '三':
            count = 3
        if count == '四':
            count = 4
        if poker == '是':
            poker = '四'
        if poker == '吧' or poker == '班':
            poker='八'
        if poker == '时':
            poker='十'
        hongMatched = 0
        heiMatched = 0
        meiMatched = 0
        fangMatched = 0
        for k in range(count):
            if(len(poker) > 1):
                # 长度大于1说明不是需要点击牌，而是选择按钮
                isPoker=1
                if poker == '叫地主':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/叫地主.jpg"
                elif poker == '不要':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/不要.jpg"
                elif poker == '提示':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/提示.jpg"
                elif poker == '抢地主':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/抢地主.jpg"
                elif poker == '不叫':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/不叫.jpg"
                elif poker == '要不起':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/要不起.jpg"
                elif poker == '出牌':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/出牌.jpg"
                elif poker == '继续游戏':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/继续游戏.jpg"
                elif poker == '开始游戏':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/开始游戏.jpg"
                elif poker == '不抢':
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/不抢.jpg"
                
                result=ImageMatch.imageMatch(targetPath,templatePath)
            else:
                if hongMatched == 0:
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/红"+poker+".jpg"
                elif heiMatched == 0:
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/黑"+poker+".jpg"
                elif meiMatched == 0:
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/梅"+poker+".jpg"
                elif fangMatched == 0:
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/红"+poker+".jpg"
                result=ImageMatch.imageMatch(targetPath,templatePath)
                if (result[0] < 0 and hongMatched == 0) or (poker == '尖' and result[0] >  720):
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/黑"+poker+".jpg"
                    result=ImageMatch.imageMatch(targetPath,templatePath)
                if (result[0] < 0 and heiMatched == 0)or (poker == '尖' and result[0] >  720):
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/梅"+poker+".jpg"
                    result=ImageMatch.imageMatch(targetPath,templatePath)
                if (result[0] < 0 and meiMatched == 0)or (poker == '尖' and result[0] >  720):
                    templatePath="/Users/xietaotao/Documents/编码奇才/image/方"+poker+".jpg"
                    result=ImageMatch.imageMatch(targetPath,templatePath)
                if result[0] < 0:
                    continue  
                else:
                    if '红' in templatePath:
                        hongMatched=1
                    elif '黑' in templatePath:
                        heiMatched=1
                    elif '梅' in templatePath:
                        meiMatched=1
                    elif '方' in templatePath:
                        fangMatched=1
            pyautogui.click(result[0],result[1])
        pyautogui.click(930,488)
    except:
        print("matchPoker error,poker:"+poker+",count:"+str(count))

def getPoker(voiceResult):
    dict = {}
    if voiceResult == '叫地主。':
        dict['叫地主']='一'
        return dict
    if voiceResult == '不要。':
        dict['不要']='一'
        return dict
    if voiceResult == '提示。':
        dict['提示']='一'
        return dict
    if voiceResult == '抢地主。':
        dict['抢地主']='一'
        return dict
    if voiceResult == '不叫。':
        dict['不叫']='一'
        return dict
    if voiceResult == '要不起。':
        dict['要不起']='一'
        return dict
    if voiceResult == '出牌。':
        dict['出牌']='一'
        return dict
    if voiceResult == '继续游戏。':
        dict['继续游戏']='一'
        return dict
    if voiceResult == '开始游戏。':
        dict['开始游戏']='一'
        return dict
    if voiceResult == '不抢。':
        dict['不抢']='一'
        return dict
    for i in range(len(voiceResult)):
        if(voiceResult[i] == GE):
            if(i==0 or i==len(voiceResult)-1):
                continue
            dict[voiceResult[i+1]] = voiceResult[i-1]
    return dict

print("voice doudizhu begining ******************************")
targetPath = "/Users/xietaotao/Documents/编码奇才/image/全部.jpg"
time.sleep(4)


while True:
    img = pyautogui.screenshot() # x,y,w,h
    rgb_im = img.convert('RGB')
    rgb_im.save(targetPath)
    VoiceRecording.recording('output.wav')
    tencentResult =  TencentRecognition.tencentRecognition().Result
    GE = "个"
    dict = getPoker(tencentResult)
    for key,value in dict.items():
        print("poker:" + key+",poker count:" + str(value))
    for key in dict:
        matchPoker(key,dict[key])


    



    
    
