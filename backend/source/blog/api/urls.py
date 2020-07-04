from django.urls import path, include
from .views import VistaListBlog, VistaDetalleBlog

# movimientomagicos
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register('items', VistaDetalleBlog)
urlpatterns = [
    path('', VistaListBlog.as_view()),
    path('<slug>', VistaDetalleBlog.as_view())
    #path('<slug>', include(router.urls))
]
