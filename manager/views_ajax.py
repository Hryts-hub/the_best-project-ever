
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from manager.models import LikeCommentUser, Comment, Book

from manager.models import LikeBookUser as RateBookUser
from manager.forms import CommentSaveForm
from manager.permissions import IsAuthor
from manager.serializers import CommentSerializer


def add_like2comment(request, comment_id):
    if request.user.is_authenticated:
        LikeCommentUser.objects.create(user=request.user, comment_id=comment_id)
        comment = Comment.objects.get(id=comment_id)
        count_likes = comment.likes
        return JsonResponse(
            {"likes": count_likes},
            status=status.HTTP_201_CREATED
        )
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


# def delete_comment(request, comment_id):
#     if request.user.is_authenticated:
#         comment = Comment.objects.get(id=comment_id)
#         if request.user == comment.author:
#             comment.delete()
#             return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
#         return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
#     return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


# class DeleteComment(APIView):
#     def delete(self, request, comment_id):
#         if request.user.is_authenticated:
#             comment = Comment.objects.get(id=comment_id)
#             if request.user == comment.author:
#                 comment.delete()
#                 return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
#             return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
#         return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteComment(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


def delete_book(request):
    if request.user.is_authenticated:
        book = Book.objects.get(slug=request.GET.get("slug"))
        if request.user in book.authors.all():
            book.delete()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


def add_rate(request):
    if request.user.is_authenticated:
        RateBookUser.objects.create(
            user=request.user,
            book_id=request.GET.get("slug"),
            rate=request.GET.get("rate"))
        book = Book.objects.get(slug=request.GET.get("slug"))
        rate = book.rate
        count_rated_users = book.count_rated_users
        return JsonResponse(
            {"rate": rate, "count_rated_users": count_rated_users},
            status=status.HTTP_201_CREATED
        )
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


def add_comment(request):

    if request.user.is_authenticated:
        cf = CommentSaveForm(data=request.POST)
        comment = cf.save(commit=False)
        # comment.book_id = Book.objects.get(slug=request.GET.get("slug")).slug
        comment.author = request.user
        comment = cf.save(commit=True)
        comment.save()
        id = comment.id
        text = comment.text
        date = comment.date
        # author = comment.author
        # print(author)
        likes = comment.likes
        return JsonResponse(
            {"id": id,
             "text": text,
             "date": date,
             # "author": author,
             "likes": likes},
            status=status.HTTP_201_CREATED
        )
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)