import random

from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import list_route

from app1.models import RealTimeNum, SavedNum
from app1.serializers import RealTimeNumSerializer, SavedNumSerializer


class RealTimeNumViewSet(viewsets.ModelViewSet):

    serializer_class = RealTimeNumSerializer
    queryset = RealTimeNum.objects.all()

    @list_route(['GET'])
    def random_nums(self, request):
        ten_nums = RealTimeNum.create_10_nums()
        return Response(RealTimeNumSerializer(ten_nums, many=True).data)


class SavedNumViewSet(viewsets.ModelViewSet):

    serializer_class = SavedNumSerializer
    queryset = SavedNum.objects.all()

    @list_route(['POST'])
    def batch_saved(self, request):
        data = request.data
        SavedNumSerializer.batch_post(data)
        return Response({
            "result": "success"
        })
