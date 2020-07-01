from django.urls import path
from .views import BooksListView, BooksDetailView, charge, SearchResultListView

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<uuid:pk>', BooksDetailView.as_view(), name='books_detail'),
    path('charge/', charge, name='charge'),
    path('search/', SearchResultListView.as_view(), name='search_results'),
]
