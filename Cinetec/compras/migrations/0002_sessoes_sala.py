# Generated by Django 5.0.3 on 2024-05-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessoes',
            name='sala',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
