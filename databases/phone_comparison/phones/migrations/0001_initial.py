# Generated by Django 2.1.7 on 2019-03-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Модель телефона')),
                ('price', models.IntegerField()),
                ('os', models.CharField(max_length=64, verbose_name='Операционная система')),
                ('resolution', models.CharField(max_length=64, verbose_name='Разрешение экрана')),
                ('camera', models.CharField(max_length=64, verbose_name='Камера')),
                ('ram', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Producer'),
        ),
    ]
