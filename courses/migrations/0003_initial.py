# Generated by Django 4.2.3 on 2023-11-12 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("assignments", "0002_initial"),
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_courses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                related_name="student_course",
                through="courses.Enrollment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="completedlesson",
            name="lesson",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.lesson"
            ),
        ),
        migrations.AddField(
            model_name="completedlesson",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="completedcourse",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.course"
            ),
        ),
        migrations.AddField(
            model_name="completedcourse",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="chapter_quiz",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz",
                to="assignments.quiz",
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.course"
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="enrollment",
            unique_together={("course", "student")},
        ),
        migrations.AlterUniqueTogether(
            name="completedlesson",
            unique_together={("user", "lesson")},
        ),
        migrations.AlterUniqueTogether(
            name="completedcourse",
            unique_together={("user", "course")},
        ),
        migrations.AlterUniqueTogether(
            name="certificate",
            unique_together={("user", "course")},
        ),
    ]
