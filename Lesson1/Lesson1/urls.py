from django.conf.urls import include, url
import HelloDjango.views

urlpatterns = [
    url(r'^$', HelloDjango.views.index, name="index"),
     url(r'^home$', HelloDjango.views.index, name="home"),
]
