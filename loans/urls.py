from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, BorrowerViewSet, InquiryViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'borrowers', BorrowerViewSet)
router.register(r'inquiries', InquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]