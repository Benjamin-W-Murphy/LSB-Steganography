import numpy as np
from PIL import Image


# 将密文图片基于混沌Logistic映射加密算法加密
# 0<x<1 , 3.5699<u<4 , times为迭代次数
def logistic(img, x, u, times):
    m = img.size[0]
    n = img.size[1]
    for i in range(1, times):
        x = u * x * (1 - x)
    array = np.zeros(m * n)
    array[1] = x
    for i in range(1, m * n - 1):
        array[i + 1] = u * array[i] * (1 - array[i])
    array = np.array(array * 255, dtype='uint8')
    code = np.reshape(array, (m, n))
    xor = img ^ code
    v = xor
    return v


# RGB密文图像加密
def logistic_img(img):
    # 定义logistic运算参数
    x = 0.1
    u = 4
    times = 500
    # 将图片分割成三个颜色通道
    b, g, r = img.split()
    # 将三通道色分开进行置乱
    b = logistic(b, x, u, times)
    g = logistic(g, x, u, times)
    r = logistic(r, x, u, times)
    # 将置乱后的信息从矩阵转会单通道图像
    b = Image.fromarray(b)
    g = Image.fromarray(g)
    r = Image.fromarray(r)
    # 恢复RGB图像
    cimg = Image.merge("RGB", (b, g, r))
    return cimg


# 灰度图密文加密
def logistic_gray_img(img):
    # 定义logistic运算参数
    x = 0.1
    u = 4
    times = 500
    # 将三通道色分开进行置乱
    c = logistic(img, x, u, times)
    # 将置乱后的信息从矩阵转会单通道图像
    cimg = Image.fromarray(c)
    return cimg


# 二值密文图像加密
def logistic_binary_img(img):
    # 定义logistic运算参数
    x = 0.1
    u = 4
    times = 500
    carray = logistic(img, x, u, times)
    cimg = Image.fromarray(carray)
    return cimg
