# Generated by Django 4.2.2 on 2023-07-09 21:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('image', models.URLField()),
                ('autor', models.CharField(max_length=50)),
                ('posted', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de carga de la imagen')),
            ],
            options={
                'verbose_name': 'página',
                'verbose_name_plural': 'páginas',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
