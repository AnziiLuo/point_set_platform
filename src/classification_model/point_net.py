#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project: point_set_platform 
@Author: anzii.Luo
@Describe: 
@Date: 2021/8/3
"""
import tensorflow as tf


class PointNet:
    def __init__(self, batch_size, num_point):
        """
        模型初始化
        :param batch_size:
        :param num_point:
        """
        self.batch_size = batch_size
        self.num_point = num_point
        self.point_pl = tf.placeholder(
            dtype=tf.float32, shape=(batch_size, num_point, 3)
        )
        self.label_pl = tf.placeholder(dtype=tf.int32, shape=batch_size)

    def get_placeholder(self):
        """
        获取输入占位符
        :return:
        """
        return self.point_pl, self.label_pl

    def get_model(self):
        """
        获取模型
        :return:
        """
        pass

    def _input_transform_net(self):
        """
        输入转换网络，是一个多层卷积网络
        :return:
        """
        # 增加一维以进行卷积运算
        input_data = tf.expand_dims(input=self.point_pl, axis=-1)
