from django.contrib import admin
from .models import User, Book, BookDetails, BorrowedBooks

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'membership_date')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'published_date', 'genre')


@admin.register(BookDetails)
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'number_of_pages', 'publisher', 'language')

@admin.register(BorrowedBooks)
class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')

