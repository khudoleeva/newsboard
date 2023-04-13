# Generated by Django 4.1.7 on 2023-04-09 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_rename_date_post_new_date_rename_name_post_new_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='one_to_many_new',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.new'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='one_to_many_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]