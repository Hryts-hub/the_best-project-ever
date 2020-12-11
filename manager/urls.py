from django.urls import path

from manager.views import hello, MyPage, AddLike, AddLike2Comment

urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path("add_like/<int:id>/", AddLike.as_view(), name="add-like"),
    path("add_like_to_comment/<int:id>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
    path("", MyPage.as_view(), name="the-main-page"),
]