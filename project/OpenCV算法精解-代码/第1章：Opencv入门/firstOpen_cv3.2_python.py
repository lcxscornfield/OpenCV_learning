# -*- coding: utf-8 -*-
import cv2
import sys
#主函数
if __name__ =="__main__":
    if len(sys.argv) > 1:
        #输入图像
        image = cv2.imread(sys.argv[1],cv2.IMREAD_ANYCOLOR)
    else:
        print "Usge:python firstOpenCV3.py imageFile"
    #显示图像
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destoryAllWindos()
