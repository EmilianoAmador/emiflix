# Generated by Django 3.2.11 on 2022-01-12 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videoproxy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video ', 'verbose_name_plural': 'Published Videos'},
        ),
    ]
