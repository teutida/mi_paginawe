# Generated by Django 3.0.6 on 2020-06-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200609_0127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriatas',
            options={'ordering': ['titulo'], 'verbose_name': 'categoriatas', 'verbose_name_plural': 'categoriasas'},
        ),
        migrations.RenameField(
            model_name='categoriatas',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
