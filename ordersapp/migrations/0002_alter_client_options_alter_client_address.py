# Generated by Django 4.2.5 on 2023-10-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'покупателя', 'verbose_name_plural': 'покупатели'},
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(default='', max_length=300, verbose_name='Адрес'),
        ),
    ]
