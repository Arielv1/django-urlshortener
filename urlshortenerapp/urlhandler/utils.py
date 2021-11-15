from django.conf import settings
from random import choice
from string import ascii_letters, digits
import hashlib

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)
salt = 0
POSSIBLE_CHARS = ascii_letters + digits

def compress_url(model, string):
    # Create salt to add volatility
    salt = choice(POSSIBLE_CHARS).encode()

    # Generate short url cropped by SIZE value
    short_url = hashlib.sha256(string.encode() + salt).hexdigest()[:SIZE]

    # Small chance that the random short url has already been generated -> generate again
    model_class = model.__class__
    if model_class.objects.filter(short=short_url).exists():
        return compress_url(model, string)

    return short_url
