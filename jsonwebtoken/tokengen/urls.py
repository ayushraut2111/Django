from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView

router=DefaultRouter()

router.register('student',views.student_api,basename="student")

urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view())

]


# http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"
# http POST http://127.0.0.1:8000/student/ 'Authorization:Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxODMxNjc3LCJpYXQiOjE2OTE4MzEzNzcsImp0aSI6IjU1MDYzZWFjOTZkODQwYWU5NDVhY2I2ZWVmZjJjMTkyIiwidXNlcl9pZCI6MX0.V-gK6QPzNKAy-LYpLqzech1egUihBoBXqfGscjx8kRQ
# http GET http://127.0.0.1:8000/student/ 'Authorization:Token '
# http POST http://127.0.0.1:8000/verifytoken/ token=""
# http DELETE http://127.0.0.1:8000/student/1/ 'Authorization:Bearer '