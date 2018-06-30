from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class EcommerceAPI(object):

    def __init__(self):

        self.client = APIClient()
        self.api_version = 'api:v1:'

    def format_url_name(self, url):

        return self.api_version + url

    def api_get(self, params, url_name, api_format='json'):

        response = self.client.get(
            reverse(
                self.format_url_name(url_name),
                kwargs=params
            ),
            format=api_format
        )

        return response

    def api_list(self, url_name, api_format='json'):

        url = '{}'.format(
            reverse(self.format_url_name(url_name)),
        )

        response = self.client.get(
            url,
            format=api_format
        )

        return response
