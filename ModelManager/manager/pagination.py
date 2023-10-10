from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'
    max_page_size=20
    invalid_page_message='page does not exixst'