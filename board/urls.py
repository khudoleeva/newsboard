from django.urls import path
from .views import *
urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', NewDetail.as_view(), name='new'),
    path('create', NewCreate.as_view()),
    path('<int:pk>/update', NewUpdate.as_view()),
    path('<int:pk>/delete', NewDelete.as_view()),
    path('user', UserView.as_view()),
    path('comment', Comment_save),
    path('comment_save', Com.as_view()),
    path('nav', Navigat),
    path('send_com', CommentSend),
    path('del_com', CommentDel),
    path('add_group', AddGroup)
]