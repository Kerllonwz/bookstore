from django.test import TestCase
from .serializers import BookSerializer


class BookSerializerValidDataTest(TestCase):
    def test_valid_data(self):
        data = {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'published_date': '2008-08-01',
            'isbn': '9780132350884',
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_saves_correct_fields(self):
        data = {
            'title': 'The Pragmatic Programmer',
            'author': 'David Thomas',
            'published_date': '1999-10-20',
            'isbn': '9780201616224',
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'The Pragmatic Programmer')


class BookSerializerInvalidDataTest(TestCase):
    def test_missing_title(self):
        data = {
            'author': 'Robert C. Martin',
            'published_date': '2008-08-01',
            'isbn': '9780132350884',
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_missing_isbn(self):
        data = {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'published_date': '2008-08-01',
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('isbn', serializer.errors)

    def test_invalid_date_format(self):
        data = {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'published_date': 'not-a-date',
            'isbn': '9780132350884',
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('published_date', serializer.errors)

    def test_duplicate_isbn_rejected_by_validator(self):
        data = {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'published_date': '2008-08-01',
            'isbn': '9780132350884',
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        duplicate = BookSerializer(data=data)
        self.assertFalse(duplicate.is_valid())
        self.assertIn('isbn', duplicate.errors)
