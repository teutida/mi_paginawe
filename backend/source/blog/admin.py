from django.contrib import admin
from .models import Post_articulo, categoriatas, AcercaDMI
#from django.contrib.auth.urls import Group

admin.site.site_header = 'Swedish House Mayan Admin'


class postAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'slug')
    list_filter = ('titulo',)


admin.site.register(Post_articulo, postAdmin)


class categoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'slug')


admin.site.register(categoriatas, categoriaAdmin)


class infouserAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


admin.site.register(AcercaDMI, infouserAdmin)
# admin.site.unregister(Group)

# Register your models here.
