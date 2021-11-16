from django.conf import settings
from random import choice
from string import ascii_letters, digits
import hashlib
from .models import ShortLongUrl
SHORT_URL_SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)
POSSIBLE_CHARS = ascii_letters + digits


def compress_url(string):
    # Create salt to add volatility
    salt = choice(POSSIBLE_CHARS).encode()

    # Generate short url cropped by SIZE value
    short_url = hashlib.sha256(
        string.encode() + salt).hexdigest()[:SHORT_URL_SIZE]

    # Small chance that the random short url has already been generated -> generate again
    if ShortLongUrl.objects.filter(short=short_url).exists():
        return compress_url(string)

    return short_url
