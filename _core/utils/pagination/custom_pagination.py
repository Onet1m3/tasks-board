from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


__all__ = (
    'SimplePageNumberPagination',
)

class SimplePageNumberPagination(PageNumberPagination):
    page_size = 30
    page_query_param = "page"
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('payload', data)
        ]))

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'next': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=4'.format(
                        page_query_param=self.page_query_param)
                },
                'previous': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=2'.format(
                        page_query_param=self.page_query_param)
                },
                'payload': schema,
                'success': {
                    'type': 'bool',
                    'example': True,
                },
            },
        }
