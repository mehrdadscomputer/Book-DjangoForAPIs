from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_api_listview(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.data[0]["title"], "A good title")
        self.assertEqual(response.data[0]["subtitle"], "An excellent subtitle")
        self.assertEqual(response.data[0]["author"], "Tom Christie")
        self.assertEqual(response.data[0]["isbn"], "1234567890123")
        self.assertContains(response, self.book)
