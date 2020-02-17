# -*- coding: utf-8 -*-
import cv2
import sys
#主函数
#"__main__":以下为主代码，但无法在其他脚本中调用该主函数。
# https://blog.csdn.net/weixin_33980459/article/details/85815057
if __name__ =="__main__":
    if len(sys.argv) > 1:
        #输入图像
        image = cv2.imread(sys.argv[1],cv2.IMREAD_ANYCOLOR)
    else:
        print "Usge:python firstOpenCV3.py imageFile"
    #显示图像
    cv2.imshow("image",image) #读图，第一个参数为图片名称，第二个参数为函数
    cv2.waitKey(0)
    #0表示无限制等待用户触发，当触发后才会继续，如果设置其他时间，单位毫秒，则过时后运行destroyAllWindows
    cv2.destroyAllWindos()#销毁窗口