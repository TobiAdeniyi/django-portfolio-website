# Generated by Django 3.1.7 on 2021-03-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='assets/images/'),
        ),
    ]
