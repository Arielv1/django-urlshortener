from django.test import TestCase
from .models import ShortLongUrl


class ShortLongUrlTestCases(TestCase):
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

    def test_non_existing_short_url(self):
        num_to_fill = 10
        for i in range(0, num_to_fill):
            self.client.post(
                "/create/", {'url': 'https://ravkavonline.co.il'})

        short_to_test = "uftyfa"
        check = ShortLongUrl.objects.filter(short=short_to_test).exists()
        self.assertEqual(check, False)

    def test_incremented_times_used(self):
        org_url = 'https://ravkavonline.co.il'
        self.client.post(
            "/create/", {'url': 'https://ravkavonline.co.il'})
        short_url = ShortLongUrl.objects.all()[0]
        self.assertEqual(short_url.long, org_url)
