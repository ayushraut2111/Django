from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# class PageSize(PageNumberPagination):
#     page_size=2
#     max_page_size=8
#     page_size_query_param='records'

# class limitpage(LimitOffsetPagination):
#     default_limit=5

class cursorpage(CursorPagination):
    page_size=4
    max_page_size=5
    ordering='name'