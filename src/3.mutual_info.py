# 互信息评分(Mutual Information based scores)
from sklearn import metrics as mr
from skimage.io import imread
import numpy as np
from common.capture_screen import capture_screen
from constant.vars import *

ui_image = imread(ui_page_path)
print(ui_image.shape)
capture_prm = {
    'site_url': site_url,
    'window_size': format(int(ui_image.shape[1] / 2)) + 'x' + format(int(ui_image.shape[0] / 2))
}
capture_screen(capture_prm)
screen_image = imread(screen_path)
# screen_image = np.resize(screen_image, (ui_image.shape[0], ui_image.shape[1], ui_image.shape[2]))

img1 = np.reshape(ui_image, -1)
img2 = np.reshape(screen_image, -1)
print(img2.shape)
print(img1.shape)
print('计算中，请稍后...')
print(img1)
mutual_infor = mr.mutual_info_score(img1, img2)

print(mutual_infor)
print('相似度： ', str(round(mutual_infor * 100, 2)) + '%')
