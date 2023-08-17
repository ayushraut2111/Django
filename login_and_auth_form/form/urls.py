from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView

router=DefaultRouter()
router.register('student',views.student_api)


urlpatterns = [
    path('signup',views.signup.as_view()),
    path('login',views.login.as_view()),
    path('logout',views.logout.as_view()),
    path('',include(router.urls)),
    path('gettoken',obtain_auth_token),    # this is used for token authentication
    path('getjwt',TokenObtainPairView.as_view()),
    path('refreshjwt',TokenRefreshView.as_view()),
    path('verifyjwt',TokenVerifyView.as_view())
    
]
