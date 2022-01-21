# Generated by Django 3.2.11 on 2022-01-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20220112_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
