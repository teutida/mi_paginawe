from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Post_articulo
from rest_framework import viewsets
from .serializers import blogserializador


class VistaListBlog(ListAPIView):
    queryset = Post_articulo.objects.all()
    serializer_class = blogserializador


class VistaDetalleBlog(RetrieveAPIView):
    queryset = Post_articulo.objects.all()
    serializer_class = blogserializador
    lookup_field = 'slug'
