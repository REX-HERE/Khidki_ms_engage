# Generated by Django 4.0.4 on 2022-05-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_dropdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
