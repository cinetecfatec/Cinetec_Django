# Generated by Django 5.0.3 on 2024-03-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listaFilmes',
            fields=[
                ('id_filme', models.AutoField(primary_key=True, serialize=False)),
                ('nome_filme', models.CharField(max_length=50)),
                ('foto_cartaz', models.CharField(max_length=50)),
                ('trailer', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=30)),
                ('distribuidora', models.CharField(max_length=30)),
                ('duracao', models.IntegerField(verbose_name='duração')),
                ('elenco', models.CharField(max_length=200)),
                ('sinopse', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Em Cartaz'), ('B', 'Em Breve'), ('C', 'Em pausa')], max_length=1)),
                ('classificacao', models.IntegerField(verbose_name='classificação')),
            ],
        ),
    ]
