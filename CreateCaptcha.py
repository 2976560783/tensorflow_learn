import random
import numpy as np
from PIL import Image
from captcha.image import ImageCaptcha


NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOW_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
UP_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']

CAPTCHA_LIST = LOW_CASE
CAPTCHA_LEN = 4         # 验证码长度
CAPTCHA_HEIGHT = 60     # 验证码高度
CAPTCHA_WIDTH = 160     # 验证码宽度


def random_captcha_text(char_set=CAPTCHA_LIST, captcha_size=CAPTCHA_LEN):
    """
    随机生成定长字符串文本内容
    :param char_set:
    :param captcha_size:
    :return:
    """
    captcha_text = [random.choice(char_set) for i in range(captcha_size)]
    return ''.join(captcha_text)


def gen_captcha_text_and_image(width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT, save=None):
    """
    生成随机验证码图片
    :param width:
    :param height:
    :param save:
    :return:
    """
    image = ImageCaptcha(width=width, height=height)
    captcha_text = random_captcha_text()
    captcha = image.generate(captcha_text)
    if save:
        image.write(captcha_text, './img/' + captcha_text + '.jpg')
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


if __name__ == '__main__':
    t, im = gen_captcha_text_and_image(save=True)
    print(t, im.shape)




