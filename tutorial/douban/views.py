from douban.models import Actors
from douban.serializers import ActorsSerializer
from rest_framework import viewsets



class ActorsList(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class ActorDetail(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


