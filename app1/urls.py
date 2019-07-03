# -*- coding: utf-8 -*-
__author__ = u"wx628"
__copyright__ = "Copyright © 2012-2017 wx628. All Rights Reserved."

from rest_framework.routers import DefaultRouter

from app1.views import RealTimeNumViewSet, SavedNumViewSet

routers = DefaultRouter(trailing_slash=True)

routers.register(r'real-time-num', RealTimeNumViewSet, base_name="real_time_num")
routers.register(r'saved-num', SavedNumViewSet, base_name="saved_num")

urlpatterns = routers.urls
