# email_trigger/urls.py

from django.urls import path
from .views import EmailAPI

urlpatterns = [
    path('send-email/', EmailAPI.as_view(), name='send_email'),
]
