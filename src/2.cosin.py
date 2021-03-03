# 基于余弦相似度评分：把图片表示成一个向量，通过计算向量之间的余弦距离来表示两张图片的相似度
from PIL import Image
from numpy import average, linalg, dot
from common.capture_screen import capture_screen
from constant.vars import *


def get_thumbnail(image, size, greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thumbnail(image1, (image1.size[0], image1.size[1]))
    image2 = get_thumbnail(image2, (image1.size[0], image1.size[1]))
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res


ui_image = Image.open(ui_page_path)
prm = {
    'site_url': site_url,
    'window_size': format(int(ui_image.size[0] / 2)) + 'x' + format(int(ui_image.size[1] / 2))
}
capture_screen(prm)
screen_image = Image.open(screen_path)
print('计算中，请稍后...')
cosin = image_similarity_vectors_via_numpy(ui_image, screen_image)
print('相似度： ', str(round(cosin * 100, 2)) + '%')
