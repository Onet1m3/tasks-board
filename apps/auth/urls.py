from django.urls import path

from apps.auth.views import UserSignUp


urlpatterns = [
     path('user/register/', UserSignUp.as_view()),
]
