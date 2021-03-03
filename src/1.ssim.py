# 结构相似性度量
from skimage.metrics import structural_similarity
from skimage.io import imread
import cv2
from common.capture_screen import capture_screen
from constant.vars import *

ui_image = imread(ui_page_path)
capture_prm = {
    'site_url': site_url,
    'window_size': format(int(ui_image.shape[1] / 2)) + 'x' + format(int(ui_image.shape[0] / 2))
}
capture_screen(capture_prm)
screen_image = imread(screen_path)

screen_image = cv2.resize(screen_image, (ui_image.shape[1], ui_image.shape[0]), interpolation=cv2.INTER_LINEAR)

print('计算中，请稍后...')
ssim = structural_similarity(ui_image, screen_image, multichannel=True)
print('相似度： ', str(round(ssim * 100, 2)) + '%')
