from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    return json data
    So we can consume by JavaScript or Swift/Java/iOS/Android
    """
    data = {
        'id':tweet_id,
    }

    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        # put a key of content with a value of obj.content into data dict
        data['content'] = obj.content
    except:
        # put a key of message with a value of Not found into data dict
        data['message'] = 'Not found'
        status = 404
    
    return JsonResponse(data, status=status) # similar to json.dumps with content_type='application/json' from python module