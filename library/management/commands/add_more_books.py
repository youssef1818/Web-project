from django.core.management.base import BaseCommand
from django.utils import timezone
from library.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Add more diverse books to the library'

    def handle(self, *args, **kwargs):
        # New books data with diverse genres and authors
        books_data = [
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'description': 'A science fiction masterpiece about politics, religion, and power on a desert planet.',
                'isbn': '9780441172719',
                'available_copies': 4,
                'publication_date': datetime(1965, 8, 1)
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A philosophical novel about a young Andalusian shepherd and his journey to find his destiny.',
                'isbn': '9780062315007',
                'available_copies': 5,
                'publication_date': datetime(1988, 1, 1)
            },
            {
                'title': 'The Name of the Wind',
                'author': 'Patrick Rothfuss',
                'description': 'A fantasy novel following the life of Kvothe, a legendary musician and magician.',
                'isbn': '9780756404741',
                'available_copies': 3,
                'publication_date': datetime(2007, 3, 27)
            },
            {
                'title': 'The Silent Patient',
                'author': 'Alex Michaelides',
                'description': 'A psychological thriller about a woman who shoots her husband and then never speaks again.',
                'isbn': '9781250301697',
                'available_copies': 4,
                'publication_date': datetime(2019, 2, 5)
            },
            {
                'title': 'The Seven Husbands of Evelyn Hugo',
                'author': 'Taylor Jenkins Reid',
                'description': 'A novel about a reclusive Hollywood movie icon and the truth about her life and loves.',
                'isbn': '9781501161933',
                'available_copies': 3,
                'publication_date': datetime(2017, 6, 13)
            },
            {
                'title': 'Pachinko',
                'author': 'Min Jin Lee',
                'description': 'An epic historical novel following a Korean family who immigrates to Japan.',
                'isbn': '9781455563937',
                'available_copies': 4,
                'publication_date': datetime(2017, 2, 7)
            },
            {
                'title': 'The Three-Body Problem',
                'author': 'Cixin Liu',
                'description': 'A science fiction novel about humanity\'s first contact with an alien civilization.',
                'isbn': '9780765382030',
                'available_copies': 3,
                'publication_date': datetime(2014, 11, 11)
            },
            {
                'title': 'Educated',
                'author': 'Tara Westover',
                'description': 'A memoir about a woman who leaves her survivalist family and goes on to earn a PhD.',
                'isbn': '9780399590504',
                'available_copies': 5,
                'publication_date': datetime(2018, 2, 20)
            },
            {
                'title': 'The Song of Achilles',
                'author': 'Madeline Miller',
                'description': 'A retelling of the Iliad that focuses on the love story of Achilles and Patroclus.',
                'isbn': '9780062060624',
                'available_copies': 4,
                'publication_date': datetime(2011, 9, 20)
            },
            {
                'title': 'Mexican Gothic',
                'author': 'Silvia Moreno-Garcia',
                'description': 'A horror novel set in 1950s Mexico about a young woman investigating her cousin\'s claims of supernatural horrors.',
                'isbn': '9780525620785',
                'available_copies': 3,
                'publication_date': datetime(2020, 6, 30)
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
                    self.style.SUCCESS(f'Successfully added "{book_data["title"]}"')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {books_created} new books to the library')
        ) 