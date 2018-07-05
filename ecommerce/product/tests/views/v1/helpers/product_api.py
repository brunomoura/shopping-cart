from common.helpers import EcommerceAPI


class ProductAPI(EcommerceAPI):

    def __init__(self):
        EcommerceAPI.__init__(self)

    def get_by_pk(self, pk):
        url_name = 'product-detail'
        response = self.api_get(
            {'pk': pk},
            url_name
        )
        return response

    def list(self):
        url_name = 'product-list'
        response = self.api_list(
            url_name
        )
        return response
