from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import compress_url
from .models import ShortLongUrl

'''
    I've chosen to use REST framework so I could parse and read request data
    without implementing frontend (html) or forms while keeping Crsf middleware
    active.
'''


@api_view(['POST'])
def create(request):
    # Get url from json in request
    long_url = request.data['url']

    # Create and save a new url instance
    model_short_url = ShortLongUrl(long=request.data['url'])
    model_short_url.short = compress_url(long_url)
    model_short_url.times_used = 0
    model_short_url.save()

    # Return short url result
    return Response({'short_url': model_short_url.short}, 200)


@api_view(['GET'])
def look_up(request, query):
    try:
        # Attempt to fetch short url from database, then increment times_used
        url = ShortLongUrl.objects.get(short=query)
        url.times_used += 1
        url.save()
        return Response({'long': url.long, 'times_used': url.times_used}, 200)
    except:
        # If fetching failed, return not found message
        return Response({'error': 'No url was found'}, 404)
