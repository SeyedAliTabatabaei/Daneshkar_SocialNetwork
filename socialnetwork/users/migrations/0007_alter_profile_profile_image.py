# Generated by Django 5.1.4 on 2024-12-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_profile_image_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images/'),
        ),
    ]