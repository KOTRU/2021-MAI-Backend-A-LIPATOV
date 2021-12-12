from logging import log
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return render(request, 'chat/index.html')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
@csrf_exempt
def connect(request):
    # In connect handler we must authenticate connection.
    # Here we return a fake user ID to Centrifugo to keep tutorial short.
    # More details about connect result format can be found in proxy docs:
    # https://centrifugal.dev/docs/server/proxy#connect-proxy
    print(request.body)
    response = {
        'result': {
            'user': 'tutorial-user'
        }
    }
    return JsonResponse(response)

@csrf_exempt
def publish(request):
    # In publish handler we can validate publication request initialted by a user.
    # Here we return an empty object – thus allowing publication.
    # More details about publish result format can be found in proxy docs:
    # https://centrifugal.dev/docs/server/proxy#publish-proxy
    response = {
        'result': {}
    }
    return JsonResponse(response)

@csrf_exempt
def subscribe(request):
    # In subscribe handler we can validate user subscription request to a channel.
    # Here we return an empty object – thus allowing subscription.
    # More details about subscribe result format can be found in proxy docs:
    # https://centrifugal.dev/docs/server/proxy#subscribe-proxy
    response = {
        'result': {}
    }
    return JsonResponse(response)        