from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('<uuid:pk>/', BookDetail.as_view()),
    path('', BookList.as_view())
]
