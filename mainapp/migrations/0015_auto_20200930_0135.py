# Generated by Django 3.1.1 on 2020-09-30 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20200930_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]