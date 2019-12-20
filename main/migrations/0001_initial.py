# Generated by Django 3.0 on 2019-12-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Categoria')),
                ('subcategoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Subcategoria')),
            ],
        ),
    ]
