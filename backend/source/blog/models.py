from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator
#from django.core.urlres import reverse


def slug_autogen(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class categoriatas(models.Model):
    titulo = models.CharField(max_length=30, unique=True)
    # para que el autslug funcione tengo que agregarle la propiedad null and blank, unique es para que no se repita solamente
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['titulo', ]
        verbose_name = 'categoriatas'
        verbose_name_plural = 'categoriasas'

    def __str__(self):
        return self.titulo


class Post_articulo(models.Model):
    titulo = models.CharField(blank=True, null=True, max_length=255)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='autorsito')
    categoria = models.ForeignKey(
        categoriatas, on_delete=models.CASCADE, verbose_name='categorita')
    descripcion = models.TextField(blank=True, null=True, max_length=255)
    cuerpo = RichTextUploadingField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(
        auto_now_add=True, verbose_name='fecha publicacion')
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name='publicacion actualizada:')
    slug = models.SlugField(max_length=200, null=True,
                            blank=True, verbose_name='texto_bonis')

    def __str__(self):
        return self.titulo


class AcercaDMI(models.Model):
    titulo = models.CharField(blank=False, null=True, max_length=255)
    foto_perfil = models.ImageField(upload_to='photos_admin')
    estudios = models.TextField(null=True, max_length=255)
    descripcion_minimus = models.TextField(
        blank=True, null=True, max_length=500)
    facebook = models.URLField(
        max_length=200, blank=True, verbose_name='facebook')
    web_page = models.URLField(
        max_length=200, blank=True, verbose_name='pagina web')
    twitter = models.URLField(
        max_length=200, blank=True, verbose_name='twitter')
    linkidn = models.URLField(
        max_length=200, blank=True, verbose_name='linkidn')
    slug = models.SlugField(blank=True, max_length=200)

    def __str__(self):
        return self.titulo


# invocacion pre guardado de mi models callbacks
pre_save.connect(slug_autogen, sender=Post_articulo)
pre_save.connect(slug_autogen, sender=categoriatas)
pre_save.connect(slug_autogen, sender=AcercaDMI)


# class Meta:
#   verbosa_name='Post_article'
