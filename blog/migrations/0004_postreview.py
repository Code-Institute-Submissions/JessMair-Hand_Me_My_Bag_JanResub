# Generated by Django 3.2.15 on 2022-08-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220812_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
