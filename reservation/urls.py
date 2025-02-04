from django.urls import path
from .views import BookingView, MenuView

urlpatterns = [
    path('bookings/', BookingView.as_view()),
    path('menu/', MenuView.as_view())
]
