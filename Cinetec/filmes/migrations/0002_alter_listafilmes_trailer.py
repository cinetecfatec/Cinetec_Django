# Generated by Django 5.0.3 on 2024-03-25 20:16

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listafilmes',
            name='trailer',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
