# Generated by Django 5.0.7 on 2024-07-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('published_at', models.DateField()),
                ('isbn', models.CharField(max_length=100)),
                ('available_copies', models.IntegerField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='./covers')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]