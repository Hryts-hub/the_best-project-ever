from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from manager.models import Book, LikeCommentUser, Comment
from manager.models import LikeBookUser as RateBookUser


def hello(request, name="filipp", digit=None):
    if digit is not None:
        return HttpResponse(f"digit is {digit}")
    return HttpResponse(f"hello {name}")


class MyPage(View):
    def get(self, request):
        context = {}
        comment_query = Comment.objects.select_related("author")
        comments = Prefetch("comments", comment_query)
        context['books'] = Book.objects.prefetch_related("authors", comments)
        context['range'] = range(1, 6)
        return render(request, "index.html", context)


class AddLike2Comment(View):
    def get(self, request, id_book, id_comment, location=None):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id_comment)
        if location is None:
            return redirect("the-main-page")
        return redirect("book-detail", id=id_book)


class AddRate2Book(View):  #
    def get(self, request, id, rate, location=None):
        if request.user.is_authenticated:
            RateBookUser.objects.create(user=request.user, book_id=id, rate=rate)
        if location is None:
            return redirect("the-main-page")
        return redirect("book-detail", id=id)


class BookDetail(View):
    def get(self, request, id):
        comment_query = Comment.objects.annotate(count_like=Count("users_like")).select_related("author")
        comments = Prefetch("comments", comment_query)
        book = Book.objects.prefetch_related("authors", comments).get(id=id)
        return render(request, "book_detail.html", {"book": book, "range": range(1, 6)})
