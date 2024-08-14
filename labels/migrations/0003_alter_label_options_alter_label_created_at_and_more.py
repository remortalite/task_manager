# Generated by Django 5.0.7 on 2024-08-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_label_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
    ]
