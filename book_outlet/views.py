from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", context={"books": books})


def book_detail(request, slug: str):
    # try:
    #     book = Book.objects.get(pk=id)
    # except ObjectDoesNotExist as e:
    #     raise Http404("Book doesn't exist") from e

    book = get_object_or_404(Book, slug=slug)
    context = {"title": book.title, "author": book.author, "rating": book.rating, "is_bestselling": book.is_bestselling}
    return render(request, "book_outlet/book_detail.html", context=context)
