# coding=utf-8
import numpy as np
from CreateCaptcha import gen_captcha_text_and_image
from CreateCaptcha import CAPTCHA_HEIGHT, CAPTCHA_WIDTH, CAPTCHA_LEN, CAPTCHA_LIST

# a = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])
# print(a.shape)
# print(np.mean(a, -1).flatten())
# a = np.zeros(2*3)
# print(a)


def convert2gray(img):
    """
    图片转黑白， 3维转1维
    :param img:
    :return:
    """
    # 表示3维彩色图片
    if len(img.shape) > 2:
        img = np.mean(img, -1)
    return img


def text2vec(text, captcha_len=CAPTCHA_LEN, captcha_list=CAPTCHA_LIST):
    """
    验证码文本转向量
    :param text:
    :param captcha_len:
    :param captcha_list:
    :return:
    """
    text_len = len(text)
    if text_len > captcha_len:
        raise ValueError('验证码最长4个字符')
    vector = np.zeros(captcha_len * len(captcha_list))
    for i in range(text_len):
        vector[captcha_list.index(text[i]) + i * len(captcha_list)] = 1
    return vector


def vec2text(vec, captcha_list=CAPTCHA_LIST, captcha_len=CAPTCHA_LEN):
    """
    验证码向量转文本
    :param vec:
    :param captcha_list:
    :param captcha_len:
    :return:
    """
    vec_idx = vec
    text_list = [captcha_list[i % len(captcha_list)] if vec_idx[i] else '' for i in range(len(vec_idx))]
    return ''.join(text_list)


def wrap_gen_captcha_text_and_image(shape=(CAPTCHA_HEIGHT, CAPTCHA_WIDTH, 3)):
    """
    返回特定shape照片
    :param shape:
    :return:
    """
    while True:
        text, image = gen_captcha_text_and_image()
        if image.shape == shape:
            return text, image


def get_next_batch(batch_count=60, width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT):
    """
    获取训练图片组
    :param batch_count:
    :param width:
    :param height:
    :return:
    """
    batch_x = np.zeros([batch_count, width * height])
    batch_y = np.zeros([batch_count, CAPTCHA_LEN * len(CAPTCHA_LIST)])

    for i in range(batch_count):
        text, image = wrap_gen_captcha_text_and_image()
        # 存储 字符串 值
        batch_y[i:] = text2vec(text)

        # 图片值
        image = convert2gray(image)
        batch_x[i:] = image.flatten() / 255

    return batch_x, batch_y


if __name__ == '__main__':
    x, y = get_next_batch(batch_count=2)
    print(y)


# a = text2vec('ajdk')
# print(a)
#
# b = vec2text(a)
# print(b)







