#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project: point_set_platform 
@Author: anzii.Luo
@Describe: minio操作工具
@Date: 2021/8/3
"""
from minio import Minio
from minio.error import S3Error


def upload_file(client: Minio, bucket, remote_file_name, local_file_path):
    """
    上传文件到minio
    :param client:
    :param bucket: 桶名（目录）
    :param remote_file_name: 上传后文件名
    :param local_file_path: 本地文件名
    :return:
    """
    # 检查桶是否存在
    found = client.bucket_exists(bucket_name=bucket)
    if not found:
        client.make_bucket(bucket_name=bucket)

    try:
        client.fget_object(
            bucket_name=bucket, object_name=remote_file_name, file_path=local_file_path
        )
    except S3Error as exc:
        raise exc
