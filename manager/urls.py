from django.urls import path
from manager.views import MyPage, AddLike2Comment, AddRate2Book, BookDetail, AddBook, AddComment, book_delete, \
    UpdateBook, comment_delete, UpdateComment, RegisterView, UpdateBookAuthor, GenreFilter, personal_view, git_callback
from manager.views import LoginView, logout_user
from manager.views_ajax import add_like2comment, delete_comment, delete_book, add_rate, add_comment

urlpatterns = [
    path("books_genre/<str:genre>/", GenreFilter.as_view(), name="books-genre"),
    path("add_like_to_comment/<str:slug>/<int:id_comment>/",  #
         AddLike2Comment.as_view(),
         name="add-like-to-comment-location"),
    path("add_rate_to_book/<str:slug>/<int:rate>/",
         AddRate2Book.as_view(),
         name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(),
         name="add-rate-location"),
    path("rate_ajax/", add_rate),  #
    path("book_view_detail/<str:slug>/",
         BookDetail.as_view(),
         name="book-detail"),
    path("add_book/",
         AddBook.as_view(),
         name="add-book"),
    path("add_comment_location/<str:slug>/",  #
         AddComment.as_view(),
         name="add-comment-location"),
    path("add_comment_ajax", add_comment),  #
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", logout_user, name="logout"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("delete_book_ajax", delete_book),
    path("update_book/<str:slug>/", UpdateBook.as_view(), name="update-book"),
    path("update_book_author/<str:slug>/",
         UpdateBookAuthor.as_view(),
         name="update-book-author"),
    path("delete_comment/<str:slug>/<int:id_comment>/",
         comment_delete,
         name="delete-comment"),
    path("update_comment/<str:slug>/<int:id_comment>/",
         UpdateComment.as_view(),
         name="update-comment"),
    path("add_like2comment_ajax/<int:comment_id>", add_like2comment),  #
    path("delete_comment_ajax/<int:comment_id>", delete_comment),  #
    path("personal_page/", personal_view, name="the-personal-page"),
    path("git/", git_callback, name="git-callback"),
    path("", MyPage.as_view(), name="the-main-page"),
]

