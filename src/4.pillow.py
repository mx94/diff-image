# 数值越小，相似度越高
from PIL import Image
import math
import operator
from functools import reduce
from common.capture_screen import capture_screen
from constant.vars import *

ui_image = Image.open(ui_page_path)
prm = {
    'site_url': site_url,
    'window_size': format(int(ui_image.size[0] / 2)) + 'x' + format(int(ui_image.size[1] / 2))
}

capture_screen(prm)
screen_image = Image.open(screen_path)

h1 = ui_image.histogram()
h2 = screen_image.histogram()

result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))

print(result)
