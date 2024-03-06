# Generated by Django 5.0.1 on 2024-03-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='category',
            field=models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('MA', 'Торговцы'), ('GM', 'Гилдмастеры'), ('GI', 'Квестгиверы'), ('BS', 'Кузнецы'), ('TA', 'Кожевники'), ('PB', 'Зельевары'), ('SM', 'Мастера заклинаний')], default='TN', max_length=2, verbose_name='Категория'),
        ),
    ]
