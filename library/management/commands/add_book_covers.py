import os
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.base import ContentFile
from library.models import Book

class Command(BaseCommand):
    help = 'Add cover images to existing books'

    def handle(self, *args, **kwargs):
        # Dictionary mapping book titles to their cover image URLs
        book_covers = {
            'The Great Gatsby': 'https://covers.openlibrary.org/b/id/6883210-L.jpg',
            '1984': 'https://covers.openlibrary.org/b/id/8575691-L.jpg',
            'To Kill a Mockingbird': 'https://covers.openlibrary.org/b/id/8709951-L.jpg',
            'The Hobbit': 'https://covers.openlibrary.org/b/id/8406786-L.jpg',
            'Pride and Prejudice': 'https://covers.openlibrary.org/b/id/8701737-L.jpg',
            'The Catcher in the Rye': 'https://covers.openlibrary.org/b/id/8739161-L.jpg',
            'One Hundred Years of Solitude': 'https://covers.openlibrary.org/b/id/8709106-L.jpg',
            'The Lord of the Rings': 'https://covers.openlibrary.org/b/id/8406164-L.jpg'
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