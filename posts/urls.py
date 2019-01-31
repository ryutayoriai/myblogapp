from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'posts'
urlpatterns = [
        url(r'^$',views.index, name='index'),
#       url(r'^$', views.post_list, name='post_list'),
#	path('', views.IndexView.as_view(), name='index'),
#	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
