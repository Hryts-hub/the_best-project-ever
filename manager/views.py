from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from manager.forms import BookForm, CustomAuthenticationForm, CommentForm
from manager.models import LikeCommentUser, Comment
from manager.models import Book as Book
from manager.models import LikeBookUser as RateBookUser


def hello(request, name="filipp", digit=None):
    if digit is not None:
        return HttpResponse(f"digit is {digit}")
    return HttpResponse(f"hello {name}")


class MyPage(View):
    def get(self, request):
        context = {}
        books = Book.objects.prefetch_related("authors")
        context['books'] = books.order_by("-rate", "date")
        context['range'] = range(1, 6)
        context['form'] = BookForm()
        context['login_form'] = AuthenticationForm()
        return render(request, "index.html", context)


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {"form": CustomAuthenticationForm})

    def post(self, request):
        user = AuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
        return redirect("the-main-page")


def logout_user(request):
    logout(request)
    return redirect("the-main-page")


class AddLike2Comment(View):
    def get(self, request, slug, id_comment, location=None):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id_comment)
        if location is None:
            return redirect("the-main-page")
        return redirect("book-detail", slug=slug)


class AddRate2Book(View):
    def get(self, request, slug, rate, location=None):
        if request.user.is_authenticated:
            RateBookUser.objects.create(user=request.user, book_id=slug, rate=rate)
        if location is None:
            return redirect("the-main-page")
        return redirect("book-detail", slug=slug)


class BookDetail(View):
    def get(self, request, slug):
        comment_query = Comment.objects.select_related("author")
        comments = Prefetch("comments", comment_query)
        book = Book.objects.prefetch_related("authors", comments).annotate(
             count_comment=Count("comments")).get(slug=slug)
        return render(request, "book_detail.html", {
            "book": book,
            "range": range(1, 6),
            "form": CommentForm()
        })


class AddBook(View):
    def post(self, request):
        if request.user.is_authenticated:
            bf = BookForm(data=request.POST)
            book = bf.save(commit=True)
            book.authors.add(request.user)
            book.save()
        return redirect("the-main-page")


# def book_delete(request, slug):
#     if request.user.is_authenticated:
#          book = Book.objects.get(slug=slug)
#          if request.user in book.authors.all():
#              book.delete()
#     return redirect("the-main-page")


# class UpdateBook(View):
#     def get(self, request, slug):
#         if request.user.is_authenticated:
#             book = Book.objects.get(slug=slug)
#             if request.user in book.authors.all():
#                 form = BookForm(instance=book)
#                 return render(request, "update_book.html", {"form": form, "slug": book.slug})
#         return redirect("the-main-page")
#
#     def post(self, request, slug):
#         if request.user.is_authenticated:
#             book = Book.objects.get(slug=slug)
#             if request.user in book.authors.all():
#                 bf = BookForm(instance=book, data=request.POST)
#                 if bf.is_valid():
#                     bf.save(commit=True)
#         return redirect("the-main-page")


class AddComment(View):
    def post(self, request, slug, location=None):
        if request.user.is_authenticated:
            # +
            cf = CommentForm(data=request.POST)
            comment = cf.save(commit=False)
            comment.book_id = Book.objects.get(slug=slug).id
            comment.author = request.user
            comment = cf.save(commit=True)
            comment.save()
        return redirect("book-detail", slug=slug)