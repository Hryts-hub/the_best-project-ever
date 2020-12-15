from django.urls import path
from manager.views import hello, MyPage, AddLike2Comment, AddRate2Book, BookDetail


urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path("add_like_to_comment/<str:slug>/<int:id_comment>/",
         AddLike2Comment.as_view(),
         name="add-like-to-comment"),
    path("add_like_to_comment/<str:slug>/<int:id_comment>/<str:location>/",
         AddLike2Comment.as_view(),
         name="add-like-to-comment-location"),
    path("add_rate_to_book/<str:slug>/<int:rate>/",
         AddRate2Book.as_view(),
         name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(),
         name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("", MyPage.as_view(), name="the-main-page"),
]