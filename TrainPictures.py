import tensorflow as tf
from datetime import datetime
from CreateTrainData import get_next_batch
from CreateCaptcha import CAPTCHA_HEIGHT, CAPTCHA_WIDTH, CAPTCHA_LEN, CAPTCHA_LIST


def weight_variable(shape, w_alpha=0.01):
    """
    初始化权值
    :param shape:
    :param w_alpha:
    :return:
    """
    initial = w_alpha * tf.random_normal(shape)
    return tf.Variable(initial)


def bais_variable(shape, b_alpha=0.1):
    """
    初始化置偏项
    :param shape:
    :param b_alpha:
    :return:
    """
    initial = b_alpha * tf.random_normal(shape)
    return tf.Variable(initial)


def conv2d(x, w):
    """
    卷积层： 局部变量线性组合， 步长为1 ， 模式’same‘
    表示卷积后图片尺寸不变， 零边距
    :param x:
    :param w:
    :return:
    """






