from django.views.generic import TemplateView
from books.models import Book


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_books'] = Book.objects.order_by('-created_at')[:6]
        context['last_books_next'] = Book.objects.order_by('-created_at')[7:13]
        return context
