from skimage.metrics import structural_similarity
import imutils
import cv2
from common.capture_screen import capture_screen
from constant.vars import *

# 加载两张图片并将他们转换为灰度
ui_image = cv2.imread(ui_page_path)
print(ui_image.shape)
capture_prm = {
    'site_url': site_url,
    'window_size': format(int(ui_image.shape[1] / 2)) + 'x' + format(int(ui_image.shape[0] / 2))
}
capture_screen(capture_prm)
screen_image = cv2.imread(screen_path)

grayA = cv2.cvtColor(ui_image, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)

# 计算两个灰度图像之间的结构相似度指数
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype('uint8')
print('SSIM:{}'.format(score))

# 找到不同点的轮廓，在被标识为“不同”的区域周围放置矩形
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[1] if imutils.is_cv3() else cnts[0]

# 找到一系列区域，在区域周围放置矩形
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(ui_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(screen_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow("Modified", screen_image)
cv2.imwrite(r'../files/result.png', screen_image)
# cv2.waitKey(0)
print('差异图片保存成功')
