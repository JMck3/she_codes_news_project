# Generated by Django 3.2.5 on 2021-08-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_newsstory_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(default='https://placedog.net/200/300'),
        ),
    ]