# Generated by Django 2.2.14 on 2021-10-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211016_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_detail',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]