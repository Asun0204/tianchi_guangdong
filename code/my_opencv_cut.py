#!/usr/bin/env python
# coding=utf-8
# Created by Asun on 2017/10/9
# Description:

import cv2

# 载入图片
FILE_2015 = '../preliminary/quickbird2015.tif'
FILE_2017 = '../preliminary/quickbird2017.tif'
# FILE_cadastral2015 = '../20170907_hint/cadastral2015.tif'
# FILE_tinysample = '../20170907_hint/tinysample.tif'

img_2015 = cv2.imread(FILE_2015)
img_2017 = cv2.imread(FILE_2017)
# img_tiny = cv2.imread(FILE_tinysample)
# img_cada = cv2.imread(FILE_cadastral2015)

print img_2015.shape

print img_2015[0,0,3]

cv2.imwrite()