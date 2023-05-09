from django.db.models import Avg, Max, Min
from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")  # ASC
    # books = Book.objects.all().order_by("-title") # DESC

    num_books = books.count()
    rating_metrics = books.aggregate(Avg("rating"), Min("rating"), Max("rating"))

    context = {
        "books": books,
        "total_number_of_books": num_books,
        "rating_metrics": rating_metrics,
    }

    return render(request, "book_outlet/index.html", context=context)


def book_detail(request, slug: str):

    # * Option 1
    # try:
    #     book = Book.objects.get(pk=id)
    # except ObjectDoesNotExist as e:
    #     raise Http404("Book doesn't exist") from e

    # * Option 2
    book = get_object_or_404(Book, slug=slug)

    context = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    }

    return render(request, "book_outlet/book_detail.html", context=context)
