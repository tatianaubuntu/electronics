# Generated by Django 5.1.3 on 2024-11-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('model', models.CharField(blank=True, max_length=150, null=True, verbose_name='модель')),
                ('release_date', models.DateTimeField(blank=True, null=True, verbose_name='дата выхода')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
