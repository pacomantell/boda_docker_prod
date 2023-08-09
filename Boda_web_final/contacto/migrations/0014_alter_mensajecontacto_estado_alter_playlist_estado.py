# Generated by Django 4.2.1 on 2023-07-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0013_alter_mensajecontacto_estado_alter_playlist_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajecontacto',
            name='estado',
            field=models.CharField(choices=[('d', 'No leído'), ('p', 'Leído')], default='d', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='estado',
            field=models.CharField(choices=[('d', 'No leído'), ('p', 'Leído')], default='d', max_length=1, verbose_name='Estado'),
        ),
    ]
