# Generated by Django 3.1.1 on 2020-09-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200926_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
