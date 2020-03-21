# Generated by Django 3.0.3 on 2020-03-21 10:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200, unique=True)),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Movies', 'Movies')], default='Music', max_length=30)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('video_file', models.FileField(default='', upload_to='')),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-uploaded_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('moderation', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
        ),
    ]