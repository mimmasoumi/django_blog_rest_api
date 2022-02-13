from django.urls import path

from blog.views import CreateCommentView, CreatePostView, DeletePostView, IndexView, ShowPostView, UpdatePostView


urlpatterns = [
    path("", IndexView.as_view()),
    path("create_post", CreatePostView.as_view()),
    path("post/<int:post_id>", ShowPostView.as_view()),
    path("update_post/<int:post_id>", UpdatePostView.as_view()),
    path("delete_post/<int:post_id>", DeletePostView.as_view()),
    path("create_comment/<int:post_id>", CreateCommentView.as_view()),
]
