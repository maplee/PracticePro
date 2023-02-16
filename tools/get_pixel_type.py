# -*- coding: utf-8 -*-
import cv2
import numpy as np
# import snowland.gis_tool.transformer
from snowland.gis_tool.transformer import utm_transformer


def get_file_name(longitude, latitude,
                  x_delta=0.2, y_delta=0.2, size_image=(10000, 10000)):
    """
    通过经纬度获得照片的名称
    :param longitude: float 经度
    :param latitude: float 纬度
    :param x_delta: 每个栅格代表实际距离（单位为米，默认为0.2，意味着一个栅格代表的经度方向距离为0.2米）
    :param y_delta: 每个栅格代表实际距离（单位为米，默认为0.2，意味着一个栅格代表的纬度方向距离为0.2米）
    :param size_image: 图片大小，默认10000 x 10000
    :return: 对应栅格图名
    """
    zone_num = int(np.round(longitude / 6) + 31)
    distance_x = int(x_delta * size_image[0])
    distance_y = int(y_delta * size_image[1])

    x = int(longitude // distance_x)
    y = int(latitude // distance_y)
    # return f'{zone_num}_{minp[0]}_{minp[1]}_{x}_{y}_{distance_x}_{distance_y}'
    return f'{zone_num}_{x}_{y}_{distance_x}_{distance_y}'


def get_pixel_type_func(zone_num, utm_x, utm_y,
                        # min_x, min_y,
                        delta_x=0.2, delta_y=0.2, size_image=(10000, 10000)):
    """
    根据utm坐标获取位置所在栅格类型
    :param zone_num: 度带
    :param utm_x: 经度的utm坐标
    :param utm_y: 纬度的utm坐标
    :param min_x: 最小的utm经度位置（弃用）
    :param min_y: 最小的utm纬度位置（弃用）
    :param delta_x: 每个栅格代表实际距离（单位为米，默认为0.2，意味着一个栅格代表的经度方向距离为0.2米）
    :param delta_y: 每个栅格代表实际距离（单位为米，默认为0.2，意味着一个栅格代表的纬度方向距离为0.2米）
    :param size_image: 图片大小，默认10000 x 10000
    :return:
    """
    distance_x = int(delta_x * size_image[0])
    distance_y = int(delta_x * size_image[1])
    block = int(utm_x // distance_x), int(utm_y // distance_y)
    ind_x = int((utm_x - block[0] * distance_x) / delta_x)
    ind_y = int((utm_y - block[1] * distance_y) / delta_y)
    # name = f"{zone_num}_{min_x}_{min_y}_{block[0]}_{block[1]}_{int(10000 * delta_x)}_{int(10000 * delta_y)}.png"
    name = f"{zone_num}_{block[0]}_{block[1]}_{int(10000 * delta_x)}_{int(10000 * delta_y)}.png"
    img = cv2.imread(f"C:/raster/{name}", cv2.CV_8U)

    return img[ind_y, ind_x]


minp = 475717.8618522096, 4446343.382336588
name = get_file_name(116.7326464, 40.1952994)

utm_x, utm_y = utm_transformer(40.1952994, 116.7326464)
zone_number = 50
res = get_pixel_type_func(zone_number, utm_x, utm_y)
word_map = ['空地', '路面', '绿化带', '隔离带']
print(word_map[res])
