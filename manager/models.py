from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(
        max_length=50,
        verbose_name="название",
        help_text="ну это типо погоняло книги"
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    authors = models.ManyToManyField(User, related_name="books")
    likes = models.PositiveIntegerField(default=0)
    users_like = models.ManyToManyField(
        User,
        through="manager.LikeBookUser",
        related_name="liked_books"
    )

    # чтобы в админке был не обджект, а название книги и ее id
    def __str__(self):
        return f"{self.title}-{self.id}"


class LikeBookUser(models.Model):
    class Meta:
        unique_together = ("user", "book")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_book_table")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="liked_user_table")
    rate = models.PositiveIntegerField(default=5)  #

    def save(self, **kwargs):
        try:
            super().save(**kwargs)
            self.book.likes += 1  #
        except:  #
            lbu = LikeBookUser.objects.get(user=self.user, book=self.book)
            lbu.rate = self.rate
            lbu.save()


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    users_like = models.ManyToManyField(
        User,
        through="manager.LikeCommentUser",
        related_name="liked_comments"
    )

    def __str__(self):
        return f"{self.book}-{self.author}-{self.date}"


class LikeCommentUser(models.Model):
    class Meta:
        unique_together = ("user", "comment")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comment_table")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="liked_comment_table")

    def save(self, **kwargs):
        try:
            super().save(**kwargs)
        except:
            LikeCommentUser.objects.get(user=self.user, comment=self.comment).delete()
            self.comment.likes -= 1
        else:
            self.comment.likes += 1
        self.comment.save()
