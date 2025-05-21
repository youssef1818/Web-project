from django.core.management.base import BaseCommand
from django.utils import timezone
from library.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Initialize library with sample data'

    def handle(self, *args, **kwargs):
        # Sample books data
        books_data = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'A story of decadence and excess, Gatsby explores the darker aspects of the Jazz Age.',
                'isbn': '9780743273565',
                'available_copies': 5,
                'publication_date': datetime(1925, 4, 10)
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'description': 'A dystopian novel about surveillance and control in a totalitarian society.',
                'isbn': '9780451524935',
                'available_copies': 3,
                'publication_date': datetime(1949, 6, 8)
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'A powerful story of racial injustice and the loss of innocence in the American South.',
                'isbn': '9780446310789',
                'available_copies': 4,
                'publication_date': datetime(1960, 7, 11)
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'description': 'A fantasy novel about the adventures of Bilbo Baggins in Middle-earth.',
                'isbn': '9780547928227',
                'available_copies': 2,
                'publication_date': datetime(1937, 9, 21)
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A romantic novel about the Bennet sisters and their suitors in Georgian England.',
                'isbn': '9780141439518',
                'available_copies': 6,
                'publication_date': datetime(1813, 1, 28)
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'description': 'A story of teenage alienation and loss of innocence in New York City.',
                'isbn': '9780316769488',
                'available_copies': 3,
                'publication_date': datetime(1951, 7, 16)
            },
            {
                'title': 'One Hundred Years of Solitude',
                'author': 'Gabriel García Márquez',
                'description': 'A multi-generational saga of the Buendía family in the mythical town of Macondo.',
                'isbn': '9780060883287',
                'available_copies': 2,
                'publication_date': datetime(1967, 5, 30)
            },
            {
                'title': 'The Lord of the Rings',
                'author': 'J.R.R. Tolkien',
                'description': 'An epic high-fantasy novel that follows the quest to destroy the One Ring.',
                'isbn': '9780618640157',
                'available_copies': 7,
                'publication_date': datetime(1954, 7, 29)
            }
        ]

        # Create books
        books_created = 0
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults={
                    'title': book_data['title'],
                    'author': book_data['author'],
                    'description': book_data['description'],
                    'available_copies': book_data['available_copies'],
                    'publication_date': book_data['publication_date']
                }
            )
            if created:
                books_created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully initialized library with {books_created} new books')
        ) 