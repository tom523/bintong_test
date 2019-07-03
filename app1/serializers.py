# -*- coding: utf-8 -*-
from rest_framework import serializers

from app1.models import RealTimeNum, SavedNum

__author__ = u"wx628"
__copyright__ = "Copyright © 2012-2017 wx628. All Rights Reserved."


class BatchUpdateCreateSerializer(serializers.ModelSerializer):

    @classmethod
    def batch_update(cls, data_list):
        ret = []
        for item in data_list:
            obj = cls(cls.Meta.model.objects.get(pk=item['id']), data=item)
            if obj.is_valid():
                ret.append(obj.save())
        return ret

    @classmethod
    def batch_post(cls, data_list):
        ret = []
        for item in data_list:
            serializer = cls(data=item)
            if serializer.is_valid():
                ret.append(serializer.save())
        return ret


class RealTimeNumSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealTimeNum
        fields = '__all__'


class SavedNumSerializer(BatchUpdateCreateSerializer):

    class Meta:
        model = SavedNum
        fields = '__all__'
