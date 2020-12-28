from django.urls import path
from manager.views import MyPage, AddLike2Comment, AddRate2Book, BookDetail, AddBook, AddComment, book_delete, \
    UpdateBook, comment_delete, UpdateComment, RegisterView  #
from manager.views import LoginView, logout_user


urlpatterns = [
    path("add_like_to_comment/<str:slug>/<int:id_comment>/<str:location>/",
         AddLike2Comment.as_view(),
         name="add-like-to-comment-location"),
    path("add_rate_to_book/<str:slug>/<int:rate>/",
         AddRate2Book.as_view(),
         name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(),
         name="add-rate-location"),
    path("book_view_detail/<str:slug>/",
         BookDetail.as_view(),
         name="book-detail"),
    path("add-book/",
         AddBook.as_view(),
         name="add-book"),
    path("add-comment-location/<str:slug>/<str:location>/",
         AddComment.as_view(),
         name="add-comment-location"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", logout_user, name="logout"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("update_book/<str:slug>/", UpdateBook.as_view(), name="update-book"),
    path("delete_comment/<str:slug>/<int:id_comment>/",
         comment_delete,
         name="delete-comment"),
    path("update_comment/<str:slug>/<int:id_comment>/",
         UpdateComment.as_view(),
         name="update-comment"),
    path("", MyPage.as_view(), name="the-main-page"),
]