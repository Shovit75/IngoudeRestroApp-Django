# Generated by Django 5.0.7 on 2024-07-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0005_alter_category_featured_alter_food_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('designation', models.CharField(max_length=128)),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
    ]
