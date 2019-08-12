from django.conf.urls import url, include
from app.users.views import *

urlpatterns = [
    url(r'^signin$', signin, name='api_signin'),
    url(r'^user_info$', user_info, name='api_user_info'),
]