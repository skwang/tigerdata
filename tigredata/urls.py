from django.conf.urls import patterns, url
import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^dorm-list/$', views.get_dorm_list, name='dorm_list'),
        url(r'^dorm-graph/$', views.get_dorm_graph, name='dorm_graph'),
        ]