# Generated by Django 3.2.11 on 2022-01-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbase', '0006_auto_20220116_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='description',
            field=models.TextField(),
        ),
    ]
