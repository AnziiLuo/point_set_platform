#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project: point_set_platform 
@Author: anzii.Luo
@Describe: 一些构建网络的工具
@Date: 2021/8/4
"""
import tensorflow as tf


def point_conv2d(
    input_data: tf.Tensor,
    num_output_channels: int,
    kernel_size: list,
    scope_name: str,
    stride: list,
    padding="SAME",
    use_xavier=True,
    stddev=1e-3,
    weight_decay=0.0,
    activation_fn=tf.nn.relu,
    bn=False,
    bn_decay=None,
    is_training=None,
):
    """
    点云二维卷积运算
    :param input_data: BxHxWxC
    :param num_output_channels: 输出维度
    :param kernel_size: 核形状 [kernel_h, kernel_w]
    :param scope_name: 运算名称
    :param stride:
    :param padding:
    :param use_xavier:
    :param stddev:
    :param weight_decay:
    :param activation_fn:
    :param bn:
    :param bn_decay:
    :param is_training:
    :return:
    """
    with tf.variable_scope(scope_name) as sc:
        kernel_h, kernel_w = kernel_size
        num_input_channels = input_data.get_shape()[-1].value
        kernel_shape = [kernel_h, kernel_w, num_input_channels, num_output_channels]
        kernel = _variable_with_weight_decay(
            variable_name="kernel",
            variable_shape=kernel_shape,
            stddev=stddev,
            wd=weight_decay,
            use_xavier=use_xavier,
        )
        stride_h, stride_w = stride


def _variable_with_weight_decay(
    variable_name, variable_shape, stddev, wd=None, use_xavier=True
):
    """
    创建带有权重衰减的初始化变量
    :param variable_name:
    :param variable_shape:
    :param stddev:
    :param wd: 衰减系数
    :param use_xavier:
    :return:
    """
    if use_xavier:
        initializer = tf.contrib.layers.xavier_initializer()
    else:
        initializer = tf.truncated_normal_initializer(stddev=stddev)
    variable = _variable_on_cpu(
        variable_name=variable_name,
        variable_shape=variable_shape,
        initializer=initializer,
    )
    if wd:
        weight_decay = tf.multiply(tf.nn.l2_loss(variable), wd, name="weight_loss")
        tf.add_to_collection("losses", weight_decay)
    return variable


def _variable_on_cpu(variable_name, variable_shape, initializer, use_fp16=False):
    """
    将变量存放在cpu中
    :param variable_name:
    :param variable_shape:
    :param initializer:
    :param use_fp16:
    :return:
    """
    with tf.device("/cpu:0"):
        data_type = tf.float16 if use_fp16 else tf.float32
        variable = tf.get_variable(
            name=variable_name,
            shape=variable_shape,
            initializer=initializer,
            dtype=data_type,
        )
    return variable
