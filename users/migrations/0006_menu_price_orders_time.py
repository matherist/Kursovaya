# Generated by Django 4.2.6 on 2024-04-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_vacancies_image_url_orders_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.CharField(default='100сом', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='time',
            field=models.CharField(default='Ко скольки или через сколько вы ожидаете (минимум 15мин)?', max_length=20),
        ),
    ]
