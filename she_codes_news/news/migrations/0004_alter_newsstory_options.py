# Generated by Django 3.2.5 on 2021-08-24 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
    ]