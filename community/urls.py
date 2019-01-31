from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'community'
urlpatterns = [
        url(r'^$',views.BoardListView.as_view(), name='home'),
        url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
        url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
        url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.CommentListView.as_view(), name='topic_comments'),
        url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
        url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/comments/(?P<comment_pk>\d+)/edit/$',
            views.CommentUpdateView.as_view(), name='edit_comment'),
        #url(r'^admin/', admin.site.urls),
]
