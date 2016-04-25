from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'algorithms'
urlpatterns = [
    url(r'^convexhull/$', views.ConvexHullView.as_view(), name='convexhull'),
    # url(r'^compute/$', views.compute, name='compute'),
    # url(r'^results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^simple/.*$', views.simple, name='simple'),
]