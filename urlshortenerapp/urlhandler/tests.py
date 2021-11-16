from django.test import TestCase
from .models import ShortLongUrl
from .utils import compress_url

class ShortLongUrlTestCases(TestCase):

    # Generate several short urls, confirm that all are unique and appear once
    def test_different_results_for_same_url(self):
        num_to_test = 10
        for i in range(0, num_to_test):
            self.client.post(
                "/create/", {'url': 'https://ravkavonline.co.il'})

        all_urls = ShortLongUrl.objects.all()
        count = 0
        for url in all_urls:
            count += len(ShortLongUrl.objects.filter(short=url.short))
        self.assertEqual(count, len(all_urls))

    '''
        Create short urls from same origin, then create another one manually
        and confirm it has unique value
    '''
    def test_non_existing_short_url(self):
        num_to_fill = 10
        for i in range(0, num_to_fill):
            self.client.post(
                "/create/", {'url': 'https://ravkavonline.co.il'})

        short_to_test = compress_url('https://ravkavonline.co.il')
        check = ShortLongUrl.objects.filter(short=short_to_test).exists()
        self.assertEqual(check, False)