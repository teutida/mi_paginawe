from rest_framework import serializers
from blog.models import Post_articulo


class blogserializador(serializers.ModelSerializer):
    class Meta:
        model = Post_articulo
        fields = ("id", 'titulo', 'autor', 'categoria', 'descripcion',
                  'cuerpo', 'fecha_publicacion', 'fecha_actualizacion', 'slug')
