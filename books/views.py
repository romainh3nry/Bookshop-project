from django.views.generic import ListView, DetailView
from .models import Book
from django.conf import settings


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
