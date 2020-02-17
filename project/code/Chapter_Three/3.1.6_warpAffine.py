# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 主函数
if __name__ == "__main__":
    image = cv2.imread("E:/project/opencv/project/code/Chapter_Three/img.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("img.jpg", image)

    # 原图的高宽
    h, w = image.shape[:2]
    # 仿射变换矩阵，缩小两倍
    A1 = np.array([[0.5, 0, 0], [0, 0.5, 0]], np.float32)
    d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)
    # 先缩小2倍再平移
    A2 = np.array([[0.5, 0, w / 4], [0, 0.5, h / 4]], np.float32)
    d2 = cv2.warpAffine(image, A2, (w, h), borderValue=125)
    # 在d2基础上，绕图像的中心点逆时针旋转30度
    A3 = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), 30, 1)
    d3 = cv2.warpAffine(image, A3, (w, h), borderValue=125)
    cv2.imshow("image", image)
    cv2.imshow("d1", d1)
    cv2.imshow("d2", d2)
    cv2.imshow("d3", d3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()