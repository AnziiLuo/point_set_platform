#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project: point_set_platform 
@Author: anzii.Luo
@Describe: minio 初始化
@Date: 2021/8/3
"""
from minio import Minio


class MinioBase:
    _client = {}

    def __init__(
        self,
        url="http://172.17.0.3:9090",
        access_key="anzii",
        secret_key="01020304",
        secure=True,
    ):
        """
        minio初始化
        :param url:
        :param access_key:
        :param secret_key:
        :param secure:
        """
        self.url = url
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure

    def get_client(self):
        """
        获取客户端
        :return:
        """
        key = self.url + self.access_key + self.secret_key
        if self._client.get(key):
            return self._client[key]
        else:
            client = Minio(
                endpoint=self.url,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=self.secure,
            )
            self._client[key] = client
            return client
