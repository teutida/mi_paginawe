# Generated by Django 3.0.6 on 2020-06-09 05:52

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categoriatas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'categoriatas',
                'verbose_name_plural': 'categoriasas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Post_articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('cuerpo', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha publicacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='publicacion actualizada:')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autorsito')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoriatas', verbose_name='categorita')),
            ],
        ),
    ]