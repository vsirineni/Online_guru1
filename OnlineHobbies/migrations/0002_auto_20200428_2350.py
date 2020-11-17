# Generated by Django 2.2.4 on 2020-04-29 04:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHobbies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_class_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='User/images')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineClassEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('online_class_name', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='OnlineClassEnroll', to='OnlineHobbies.OnlineClass')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineClassVideoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_title', models.CharField(max_length=100)),
                ('class_subtitle', models.CharField(max_length=100)),
                ('class_requirements', models.TextField(max_length=2500)),
                ('class_goal', models.TextField(max_length=2500)),
                ('class_video_links', models.CharField(max_length=25)),
                ('online_class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnlineClassVideoPage', to='OnlineHobbies.OnlineClass')),
            ],
        ),
        migrations.DeleteModel(
            name='Online_Hobbies',
        ),
    ]
