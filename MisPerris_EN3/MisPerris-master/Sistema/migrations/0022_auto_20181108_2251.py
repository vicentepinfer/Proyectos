# Generated by Django 2.1.1 on 2018-11-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0021_auto_20181108_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(default='Sistema/media/mascotas/noname.jpg', upload_to='Sistema/media/mascotas'),
        ),
    ]