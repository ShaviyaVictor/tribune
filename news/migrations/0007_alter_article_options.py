# Generated by Django 4.0.2 on 2022-03-01 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_article_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date']},
        ),
    ]
