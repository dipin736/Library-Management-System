from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserLoginView,
    UserRegistrationView,
    UserViewSet,
    BookViewSet,
    BookDetailsViewSet,
    BorrowedBooksViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'books', BookViewSet, basename='book')
router.register(r'book-details', BookDetailsViewSet, basename='book-details')
router.register(r'borrowed-books', BorrowedBooksViewSet, basename='borrowed-books')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
     path('login/', UserLoginView.as_view(), name='user-login'), 
       
]
