# Generated by Django 4.2.1 on 2023-06-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0005_delete_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre_cancion')),
                ('artista', models.CharField(max_length=250, verbose_name='nombre_artista')),
            ],
        ),
    ]
