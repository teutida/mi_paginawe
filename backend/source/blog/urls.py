from django.urls import path
from .views import index, postdetalle

# from .view import


urlpatterns = [
    path('', index.as_view(), name='casa'),
    path('blog/<slug>/', postdetalle.as_view(), name="detalle"),
]
