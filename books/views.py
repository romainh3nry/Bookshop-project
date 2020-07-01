from django.views.generic import ListView, DetailView
from .models import Book
from django.conf import settings
import stripe
from django.shortcuts import render
from django.db.models import Q

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


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


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=599,
            currency='usd',
            description=request.POST['description'],
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


class SearchResultListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
