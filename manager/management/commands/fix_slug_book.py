from django.core.management.base import BaseCommand
# from manager.models import Book, SlugBook, LikeBookUser, Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
        # books = Book.objects.prefetch_related("authors")
        #
        # arrSlugBook = [SlugBook(
        #     slug=b.slug,
        #     # id=b.id,
        #     title=b.title,
        #     date=b.date,
        #     text=b.text,
        #     # authors=b.authors.all(),
        #     # authors.add(b.authors.all()),
        #     count_rated_users=b.count_rated_users,
        #     count_all_stars=b.count_all_stars,
        #     rate=b.rate,
        #     # users_like=b.users_like,
        #         )
        #     for b in books
        #     ]
        #
        # SlugBook.objects.bulk_create(arrSlugBook)
        #

        #
        # query = Book.objects.all().values("slug", "id")
        # all_lbu = LikeBookUser.objects.all()
        # for book in query:
        #     new_set = all_lbu.filter(book_id=book['id'])
        #     for lbu in new_set:
        #         lbu.slug_id = book['slug']
        #         lbu.save()
        #

        # query = Book.objects.all().values("slug", "id")
        # all_comments = Comment.objects.all()
        # for book in query:
        #     comments = all_comments.filter(book_id=book['id'])
        #     for c in comments:
        #         c.slug_id = book['slug']
        #     Comment.objects.bulk_update(comments, ['slug_id'])


        # #  +
        # books = Book.objects.all()
        # tmp_books = SlugBook.objects.all()
        # for book in books:
        #     tmp_book = tmp_books.get(slug=book.slug)
        #     for author in book.authors.all():
        #         tmp_book.authors.add(author)
        #     tmp_book.save()
