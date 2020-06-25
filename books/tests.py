from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
            picture='test picture',
            plot='test plot'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')
        self.assertEqual(f'{self.book.picture}', 'test picture')
        self.assertEqual(f'{self.book.plot}', 'test plot')

    def test_book_list_view(self):
        response = self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books_list.html')
