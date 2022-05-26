"""

fsc_users/urls.py: urls for users app

"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.user_profile,
        name='profile'
    ),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path(
        'add_to_favourites/<int:product_id>',
        views.add_to_favourites,
        name='add_to_favourites'
    ),
    path(
        'delete_from_favourites/<int:product_id>',
        views.delete_from_favourites,
        name='delete_from_favourites'
    ),
]
