# -*- coding:utf-8 -*-
# 作者：庄立成
# 日期：2020/6/10 17:58
# 工具：PyCharm
# 文件 :serializers.py
# Python版本：3.5.2
from rest_framework import serializers
from douban.models import Actors


class ActorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors
        fields = ('id', 'name', 'birthday', 'birthplace', 'constellation',
                  'family_member', 'gender', 'image_url',
                  'other_chinese_name', 'other_english_name', 'profession',
                  'introduction')