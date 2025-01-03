# Generated by Django 5.1.4 on 2025-01-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='users.tag'),
        ),
    ]
