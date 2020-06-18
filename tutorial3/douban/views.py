from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from douban.models import Actors
import json
# Create your views here.
def index(request):
    return render(request,'show.html')


@require_http_methods(["GET"])
def method_get(request):
    if request.method == 'GET':
        actors = Actors.objects.all().order_by('id')

        line = list()
        for actor in actors:
            response = {}
            response['id'] = actor.id
            response['name'] = actor.name
            response['gender'] = actor.gender
            response['birthday'] = actor.birthday
            response['birthplace'] = actor.birthplace
            response['constellation'] = actor.constellation
            line.append(response)
        return JsonResponse(line, safe=False)