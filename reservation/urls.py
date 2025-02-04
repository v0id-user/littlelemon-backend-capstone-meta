from django.urls import path
from .views import BookingView, MenuView, SingleMenuItemView    

urlpatterns = [
    path('bookings/', BookingView.as_view()),
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view())
]
