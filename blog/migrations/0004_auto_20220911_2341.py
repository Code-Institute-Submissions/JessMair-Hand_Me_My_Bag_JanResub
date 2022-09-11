# Generated by Django 3.2.15 on 2022-09-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220812_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=3, max_length=2),
        ),
    ]
