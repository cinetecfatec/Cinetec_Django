# Generated by Django 5.0.3 on 2024-05-08 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_user_delete_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
