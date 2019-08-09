import tensorflow as tf
from datetime import datetime
from CreateTrainData import get_next_batch
from CreateCaptcha import CAPTCHA_HEIGHT, CAPTCHA_WIDTH, CAPTCHA_LEN, CAPTCHA_LIST


def weight_variable(shape, w_alpha=0.01):
    """
    ��ʼ��Ȩֵ
    :param shape:
    :param w_alpha:
    :return:
    """
    initial = w_alpha * tf.random_normal(shape)
    return tf.Variable(initial)


def bais_variable(shape, b_alpha=0.1):
    """
    ��ʼ����ƫ��
    :param shape:
    :param b_alpha:
    :return:
    """
    initial = b_alpha * tf.random_normal(shape)
    return tf.Variable(initial)


def conv2d(x, w):
    """
    ����㣺 �ֲ�����������ϣ� ����Ϊ1 �� ģʽ��same��
    ��ʾ�����ͼƬ�ߴ粻�䣬 ��߾�
    :param x:
    :param w:
    :return:
    """






