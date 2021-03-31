1.python3.6
2.pip3 install Pillow  (使用pip3安装如果超时，可以直接下载whl文件到本地install)
3.pip3 install opencv-python   (如果pip3安装失败可尝试自行下载对应版本whl安装)
4.vscode 麦克风权限
5.
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  tencentcloud-sdk-python

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  pyautogui，PyUserInput

cd "/Applications/Python 3.6/"
sudo "./Install Certificates.command"



pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple imutils

import sys  
import codecs  

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())  


6.实际控制效果并不流畅，主要受限于模板匹配的成功率的问题，如果想要变得流畅，一个办法是语音输入更加详细，例如 一个方块三，这样程序就不用遍历去匹配，匹配成功率会高很多，另外一个办法是提高cv2的模板匹配成功率，不过难度较大
7，image的截图使用自己的屏幕截图会匹配率高一点
8.模板匹配的像素以及模拟点击记得根据自己的实际情况修改
9.腾讯云语音识别需要自己申请账号