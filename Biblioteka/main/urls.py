from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, LoanViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
