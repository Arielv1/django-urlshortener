from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import compress_url
from .models import ShortLongUrl
# Create your views here.


@api_view(['POST'])
def create(request):
    long_url = request.data['url']
    model_short_url = ShortLongUrl(long=request.data['url'])
    model_short_url.short = compress_url(model_short_url, long_url)
    model_short_url.times_used = 0
    model_short_url.save()
    return Response({'short_url': model_short_url.short})


@api_view(['GET'])
def look_up(request, query):
    try:
        url = ShortLongUrl.objects.get(short=query)
        url.times_used += 1
        url.save()
        return Response({'long': url.long, 'times_used': url.times_used})
    except:
        return Response({'error': 'No url was found'})
