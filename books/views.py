from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.
class BooksListView(ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books_list'
    paginate_by = 12


class BooksDetailView(DetailView):
    model = Book
    template_name = 'books_detail.html'
    context_object_name = 'book'
