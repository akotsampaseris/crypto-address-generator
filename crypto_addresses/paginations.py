from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPageNumber(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('page_size', self.page_size),
            ('current', self.page.number),
            ('previous', self.get_previous_link()),
            ('next', self.get_next_link()),
            ('results', data)
         ]))