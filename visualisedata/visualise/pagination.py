from rest_framework.pagination import CursorPagination,PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size=10