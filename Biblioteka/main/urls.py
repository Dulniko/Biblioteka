from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, LoanViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'loans', LoanViewSet, basename="loans")
router.register(r'customer', CustomerViewSet, basename="customer")

urlpatterns = [
    path('', include(router.urls)),
]
