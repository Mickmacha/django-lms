# Generated by Django 4.2.6 on 2023-11-16 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0004_quiz_completed_quizzes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='completed_quizzes',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_quizzes', models.ManyToManyField(blank=True, related_name='completed_by_users', to='assignments.quiz')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]