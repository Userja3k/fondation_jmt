# Generated by Django 5.2 on 2025-04-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('theme', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('verses', models.TextField(help_text='Enter Bible verses separated by commas')),
                ('song_title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='archives/')),
                ('sermon_video', models.FileField(upload_to='videos/sermons/')),
                ('song_video', models.FileField(blank=True, null=True, upload_to='videos/songs/')),
            ],
            options={
                'verbose_name': 'Service archivé',
                'verbose_name_plural': 'Services archivés',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='debates/')),
                ('video', models.FileField(upload_to='videos/debates/')),
            ],
            options={
                'verbose_name': 'Débat',
                'verbose_name_plural': 'Débats',
                'ordering': ['-date'],
            },
        ),
    ]
