from django.conf.urls import url, include
from app.test_api import views

urlpatterns = [
    url(r'^test/$', views.tabla_List.as_view(), name='tabla_list'),
    url(r'^test/(?P<pk>\d+)/$', views.tabla_Detail.as_view(), name='tabla_detail'),
]