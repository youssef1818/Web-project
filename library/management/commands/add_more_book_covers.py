import os
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.base import ContentFile
from library.models import Book

class Command(BaseCommand):
    help = 'Add cover images to the new books'

    def handle(self, *args, **kwargs):
        # Dictionary mapping book titles to their cover image URLs
        book_covers = {
            'Dune': 'https://covers.openlibrary.org/b/id/12021925-L.jpg',
            'The Alchemist': 'https://covers.openlibrary.org/b/id/7890267-L.jpg',
            'The Name of the Wind': 'https://covers.openlibrary.org/b/id/6597145-L.jpg',
            'The Silent Patient': 'https://covers.openlibrary.org/b/id/12733645-L.jpg',
            'The Seven Husbands of Evelyn Hugo': 'https://covers.openlibrary.org/b/id/12548849-L.jpg',
            'Pachinko': 'https://covers.openlibrary.org/b/id/8432693-L.jpg',
            'The Three-Body Problem': 'https://covers.openlibrary.org/b/id/7890267-L.jpg',
            'Educated': 'https://covers.openlibrary.org/b/id/8740897-L.jpg',
            'The Song of Achilles': 'https://covers.openlibrary.org/b/id/8240318-L.jpg',
            'Mexican Gothic': 'https://covers.openlibrary.org/b/id/10389354-L.jpg'
        }

        books_updated = 0
        for book in Book.objects.all():
            if book.title in book_covers and not book.cover_image:
                try:
                    # Download the image
                    response = requests.get(book_covers[book.title])
                    if response.status_code == 200:
                        # Create filename
                        filename = f"{book.title.lower().replace(' ', '_')}.jpg"
                        
                        # Save the image content directly
                        book.cover_image.save(filename, ContentFile(response.content), save=True)
                        books_updated += 1
                        self.stdout.write(self.style.SUCCESS(f'Successfully added cover for "{book.title}"'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Failed to download cover for "{book.title}"'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error adding cover for "{book.title}": {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {books_updated} book covers')) 