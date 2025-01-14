# Generated by Django 4.2.3 on 2023-11-12 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="video",
                to="resources.videolesson",
            ),
        ),
        migrations.AddField(
            model_name="enrollment",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="courses.course",
            ),
        ),
    ]
