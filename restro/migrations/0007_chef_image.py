# Generated by Django 5.0.7 on 2024-07-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0006_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='image',
            field=models.ImageField(null=True, upload_to='chef_images/'),
        ),
    ]
