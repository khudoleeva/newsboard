# Generated by Django 4.1.7 on 2023-04-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_comment_switch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.CharField(choices=[('Танки', 'Танки'), ('Хилы', 'Хилы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')], max_length=20),
        ),
    ]