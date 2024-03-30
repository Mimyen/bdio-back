# Generated by Django 4.2.11 on 2024-03-29 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='TutorScheduleItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(help_text='Format: YYYY-MM-DD HH:MM:SS')),
                ('end_time', models.DateTimeField(help_text='Format: YYYY-MM-DD HH:MM:SS')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_schedule_items', to='tutor.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='TutorRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=1)),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_ratings', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_ratings', to='tutor.tutor')),
            ],
        ),
    ]
