from django.urls import path
from . import views
from .views import PostList, post_detail, comment_edit, comment_delete

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment/<int:comment_id>/edit/',
         views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
    # Added '/' at the end for consistency
]
