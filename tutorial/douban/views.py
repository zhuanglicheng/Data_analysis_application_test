from douban.models import Actors
from douban.serializers import ActorsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# 指定该模块只能用于get和post
@api_view(['GET', 'POST'])
def ActorsList(request):
    """
        列出所有的代码 actors，或创建一个新的 actor。
        """
    if request.method == 'GET':
        actors = Actors.objects.all()
        serializer = ActorsSerializer(actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ActorDetail(request, pk):
    """
        获取，更新或删除一个代码 actor
        """
    try:
        actor = Actors.objects.get(pk=pk)
    except Actors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ActorsSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorsSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


