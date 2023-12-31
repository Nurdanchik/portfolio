from django.urls import path
from .views import contact_view, inbox, home, create_post

urlpatterns = [
    path('contact/', contact_view, name='contact_view'),
    path('inbox/', inbox, name='inbox'),
    path('', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('create/', create_post_source, name='create_post_source'),
]

